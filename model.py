from transformers import pipeline

# Initialize the classifier pipeline (default returns top-1 dict)
classifier = pipeline(
    "text-classification", 
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

def predict_email_type(email_text):
    try:
        results = classifier(email_text)  # results is a list of dicts
        top_result = results[0]           # access first dict in list

        label = top_result["label"]
        score = top_result["score"]

        # Map model labels to your categories
        if label == "POSITIVE":
            mapped_label = "legit"
        elif label == "NEGATIVE":
            mapped_label = "phishing"
        else:
            mapped_label = "spam"

        return {
            "label": mapped_label,
            "confidence": round(score, 2),
        }

    except Exception as e:
        return {
            "label": "error",
            "confidence": 0.0,
            "error": str(e),
            "explanation": "An error occurred during prediction."
        }

