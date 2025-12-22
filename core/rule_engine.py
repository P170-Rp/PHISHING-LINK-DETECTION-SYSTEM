import re
from core.feature_extractor import extract_features

def analyze_url(url):
    features = extract_features(url)
    score = 0
    reasons = []

    if features["length"] > 75:
        score += 2
        reasons.append("URL is too long")

    if features["has_ip"]:
        score += 3
        reasons.append("Uses IP address")

    if not features["has_https"]:
        score += 1
        reasons.append("HTTPS not used")

    if features["dot_count"] > 5:
        score += 1
        reasons.append("Too many subdomains")

    suspicious_words = ["login", "verify", "bank", "secure", "update"]
    for word in suspicious_words:
        if word in url.lower():
            score += 2
            reasons.append(f"Suspicious keyword: {word}")

    return score, reasons
