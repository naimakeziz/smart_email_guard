# smart_email_guard
AI-powered spam &amp; phishing email detection tool
#  Smart Email Guardian

Smart Email Guardian is a web-based email analysis tool that leverages artificial intelligence to detect **phishing**, **spam**, and **legitimate (ham)** messages. It combines a secure Flask backend, a HuggingFace-based AI model, and a responsive HTML/CSS/JS frontend to provide users with real-time insights and a detailed scan history.

> Designed as a cybersecurity final project to demonstrate practical AI integration, frontend/backend development, and secure API design.

---

## 📌 Table of Contents

- [Features](#-features)
- [AI Model](#-ai-model)
- [Project Structure](#-project-structure)
- [Installation & Usage](#️-installation--usage)
- [API Reference](#-api-reference)
- [Frontend Dashboard](#️-frontend-dashboard)
- [CLI Tool](#-cli-tool)
- [Security Measures](#-security-measures)
- [Example Output](#-example-output)
- [Future Improvements](#-future-improvements)
- [Author](#-author)
- [License](#-license)

---

## Features

- AI-Powered Email Classification (Phishing, Spam, Legit)
- Interactive Web Dashboard (scan + view history)
- API endpoint for programmatic analysis
- CLI Tool for quick testing
-Token-based authentication for secure API access
-  Confidence scores and explanations for transparency
-  Input sanitization and secure coding practices

---

##  AI Model

- **Model Type:** BERT-based email classifier
- **Library:** [HuggingFace Transformers](https://huggingface.co/)
- **Input:** Raw email text
- **Output:** Label (`phishing`, `spam`, `legit`), confidence, and explanation

Example:
```json
{
  "label": "phishing",
  "confidence": 0.94,
  "explanation": "Suspicious link and urgency detected"
}
````

---

## 📁 Project Structure

```
smart_email_guard/
│
├── templates/              # Jinja2 HTML files (index.html, results.html)
├── static/                 # External CSS and JS
│   ├── style.css
│   └── script.js
│
├── model.py                # HuggingFace model logic
├── app.py                  # Flask app (routing, scanning)
├── api.py                  # API routes and token authentication
├── cli.py                  # CLI interface for testing scans
├── utils.py                # Input sanitization and validation
├── history.json            # Scan history (stored locally)
├── requirements.txt        # Dependencies
└── README.md               # Project description (this file)
```

---

## ⚙️ Installation & Usage

### 1. Clone and Setup


git clone https://github.com/naimakeziz/smart_email_guard.git
cd smart_email_guard
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt


### 2. Run the Web App


python app.py


Then go to: [http://localhost:5000](http://localhost:5000)

---

## 🔗 API Reference

POST /api/scan

### Headers:


{"Content-Type": "application/json"}


### Body:


{
  "api_key": "YOUR_API_KEY",
  "email_text": "Hello, click this link to verify your account..."
}
```

### Response:


{
  "label": "phishing",
  "confidence": 0.96,
  "explanation": "Detected phishing based on keywords and links"
}


*  Token-based protection is enabled
*  Invalid or missing API key returns 403

---

##  Frontend Dashboard

### Features:

*  Email input + scan button
*  Result display with label, confidence, and explanation
*  History tab with past scan records
*  Export history as JSON
*  Responsive design (mobile/tablet/desktop)

---

##  CLI Tool

Run the CLI tool to scan emails directly from the terminal:


python cli.py


Sample interaction:


Enter your email content: You won a prize! Click here to claim.
[+] Result: spam (88%) — Contains typical spam patterns
```

---

## 🔐 Security Measures

* ✅ **Input sanitization**: Prevent HTML/JS injection in frontend
* ✅ **API protection**: Token-based authentication
* ✅ **HTTPS support**: Use [ngrok](https://ngrok.com/) for secure local tunnels
* ✅ **Validation**: All API requests are validated (length, encoding, format)
* ✅ **Threat model documented**: See `security_notes.md` (optional)

---

## 📊 Example Output

### Web View

| Email Excerpt              | Label    | Confidence | Explanation                       |
| -------------------------- | -------- | ---------- | --------------------------------- |
| *"Click here to reset..."* | phishing | 0.94       | Suspicious link and urgency terms |
| *"You won a prize..."*     | spam     | 0.88       | Typical spam phrases detected     |
| *"Meeting at 3PM"*         | legit    | 0.97       | Neutral and harmless content      |

---

## 📌 Future Improvements

* [ ] Export PDF reports
* [ ] Admin panel for managing scan logs
* [ ] Training custom AI models
* [ ] Docker container for deployment
* [ ] Email header analysis

---

## 👩‍💻 Author

Made  by [Naima Keziz](https://github.com/naimakeziz)

* 💼 junior Cybersecurity analyste  




## 📃 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT)



