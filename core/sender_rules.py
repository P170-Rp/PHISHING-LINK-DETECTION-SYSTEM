import re

COMMON_BRANDS = [
    "google.com",
    "microsoft.com",
    "amazon.com",
    "paypal.com",
    "facebook.com",
    "instagram.com"
]

URGENCY_KEYWORDS = [
    "urgent",
    "immediate action",
    "verify now",
    "account suspended",
    "security alert",
    "act now",
    "limited time",
    "confirm immediately",
    "your account will be closed"
]

def extract_sender_domain(sender_email):
    try:
        return sender_email.split("@")[-1].lower()
    except:
        return ""

def is_suspicious_sender_domain(domain):
    for brand in COMMON_BRANDS:
        brand_name = brand.split(".")[0]
        if brand_name in domain and domain != brand:
            return True
    return False

def analyze_sender(sender_email, email_content=""):
    score = 0
    reasons = []

    domain = extract_sender_domain(sender_email)

    if is_suspicious_sender_domain(domain):
        score += 3
        reasons.append("Suspicious sender domain (possible brand impersonation)")

    content = email_content.lower()
    for word in URGENCY_KEYWORDS:
        if word in content:
            score += 2
            reasons.append(f"Urgency / threat keyword detected: '{word}'")
    return score, reasons
    
def is_external_sender(sender_email):
    return not sender_email.lower().endswith(
        ("@gmail.com", "@yahoo.com", "@outlook.com")
    )


    
