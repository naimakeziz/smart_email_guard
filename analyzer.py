# email_guard.py
from model import predict_email_type
import re

def analyze_email(email_text):
    result = predict_email_type(email_text)

    # Add simple heuristic explanation
    suspicious_keywords = ["urgent", "password", "verify", "account", "click here", "bank", "suspend"]
    found_keywords = [word for word in suspicious_keywords if re.search(r'\b' + re.escape(word) + r'\b', email_text, re.IGNORECASE)]

    if found_keywords:
        explanation = f"Contains suspicious keywords: {', '.join(found_keywords)}"
    elif result.get("label") == "error":
        explanation = result.get("explanation", "Unknown error occurred.")
    else:
        explanation = "No suspicious indicators found. Classified as legitimate."

    result["explanation"] = explanation
    return result
