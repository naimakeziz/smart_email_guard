from model import classify_email

def main():
    print("📧 Smart Email Classifier")

    email_text = input("\nEnter email content:\n> ")

    label, score = classify_email(email_text)

    if label == "POSITIVE":
        print(f"\n✅ Result: LEGITIMATE (Confidence: {score})")
    else:
        print(f"\n⚠️ Result: SUSPICIOUS/SPAM (Confidence: {score})")

if __name__ == "__main__":
    main()
