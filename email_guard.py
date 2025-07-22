# email_guard.py (CLI tool)
from analyzer import analyze_email
import sys

def print_result(result):
    print("\n--- Scan Result ---")
    print("Label:", result.get("label"))
    print("Confidence:", f'{result.get("confidence", 0) * 100:.2f}%')
    print("Explanation:", result.get("explanation"))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 email_guard.py 'Your email message here'")
    else:
        email_text = " ".join(sys.argv[1:])
        result = analyze_email(email_text)
        print_result(result)
