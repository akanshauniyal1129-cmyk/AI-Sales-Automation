def send_email(receiver_email, subject, body):
    print("Receiver Email=", repr(receiver_email))
    if not receiver_email:
        return "Please enter a company email address."
    print("=" * 60)
    print("AI SALES AUTOMATION AGENT - EMAIL PREVIEW")
    print("=" * 60)
    print(f"To      : {receiver_email}")
    print(f"Subject : {subject}")
    print("-" * 60)
    print(body)
    print("=" * 60)
    return (
        f"Demo Mode: Email successfully generated for "
        f"{receiver_email}. "
        "Configure Gmail API credentials to enable actual email delivery.")