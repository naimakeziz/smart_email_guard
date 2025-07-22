from flask import Flask, request, jsonify, render_template
from transformers import pipeline
import json
import os
from datetime import datetime

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)

# === 🔐 API Key ===
API_KEY = "mysecret123"

def require_api_key(view_function):
    def decorated_function(*args, **kwargs):
        key = request.headers.get("X-API-KEY")
        if not key or key != API_KEY:
            return jsonify({"error": "Unauthorized - invalid or missing API key"}), 401
        return view_function(*args, **kwargs)
    decorated_function.__name__ = view_function.__name__
    return decorated_function

# === 🧠 Load spam/ham classifier ===
classifier = pipeline("text-classification", model="mrm8488/bert-tiny-finetuned-sms-spam-detection")

# === 📁 File storage helpers ===
HISTORY_FILE = "history.json"

def load_history():
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []

def save_history(history):
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=4)

scan_history = load_history()

# === 🌐 Web Interface ===
@app.route("/")
def index():
    return render_template("index.html")

# === 🔍 Scan endpoint ===
@app.route("/scan", methods=["POST"])
@require_api_key
def scan_email():
    try:
        data = request.get_json()
        text = data.get("email_text", "").strip()

        if not text:
            return jsonify({"error": "email_text is required"}), 400

        result = classifier(text)[0]
        raw_label = result["label"]
        confidence = result["score"]

        label_map = {
            "LABEL_0": "spam",
            "LABEL_1": "ham"
        }
        label = label_map.get(raw_label, "unknown")

        explanation = {
            "spam": "⚠️ Contains suspicious or spam-like content.",
            "ham": "✅ Appears to be a safe and legitimate message."
        }.get(label, "❓ Uncertain classification.")

        scan_result = {
            "label": label,
            "confidence": round(confidence, 2),
            "explanation": explanation
        }

        entry = {
            "email_text": text,
            "result": scan_result,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        scan_history.append(entry)
        save_history(scan_history)

        return jsonify(scan_result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# === 📜 History endpoint ===
@app.route("/history", methods=["GET"])
@require_api_key
def get_history():
    return jsonify(scan_history)

# === 📊 Dashboard JSON endpoint ===
@app.route("/dashboard/data")
@require_api_key
def dashboard_data():
    total = len(scan_history)
    spam = sum(1 for h in scan_history if h["result"]["label"] == "spam")
    ham = total - spam
    return jsonify({
        "total_scans": total,
        "spam_count": spam,
        "ham_count": ham,
        "spam_percent": round((spam / total) * 100, 2) if total else 0,
        "ham_percent": round((ham / total) * 100, 2) if total else 0
    })

@app.route("/dashboard", methods=["GET"])
@require_api_key
def dashboard_page():
    total = len(scan_history)
    spam = sum(1 for h in scan_history if h["result"]["label"] == "spam")
    ham = total - spam
    spam_percent = round((spam / total) * 100, 2) if total else 0
    ham_percent = round((ham / total) * 100, 2) if total else 0

    return f"""
    <html><body style='font-family: Arial; padding: 20px;'>
      <h2>📊 Scan Dashboard</h2>
      <p><strong>Total scans:</strong> {total}</p>
      <p><strong>Spam:</strong> {spam} ({spam_percent}%)</p>
      <p><strong>Ham:</strong> {ham} ({ham_percent}%)</p>
      <a href="/">🔙 Back to Home</a>
    </body></html>
    """

# === 🚀 Run app ===
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

