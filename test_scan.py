# test_scan.py
from email_guard import analyze_email

test_email = "Your bank account has been suspended! Click here to verify your password immediately."

result = analyze_email(test_email)
print(result)

