import re

# Common spelling mistakes seen in phishing
COMMON_MISTAKES = [
    "verifiy", "updte", "acount", "securty",
    "immediatly", "suport", "congratulation",
    "click hear", "login hear"
]

def analyze_grammar(email_content):
    score = 0
    reasons = []

    text = email_content.lower()

    for word in COMMON_MISTAKES:
        if word in text:
            score += 2
            reasons.append(f"Spelling mistake detected: '{word}'")

    if sum(1 for c in email_content if c.isupper()) > len(email_content) * 0.4:
        score += 2
        reasons.append("Excessive use of capital letters")


    if "!!!" in email_content or "???" in email_content:
        score += 1
        reasons.append("Excessive punctuation detected")

    sentences = re.split(r'[.!?]', email_content)
    broken = [s for s in sentences if 0 < len(s.split()) < 3]

    if len(broken) >= 2:
        score += 2
        reasons.append("Poor sentence structure detected")

    return score, reasons
