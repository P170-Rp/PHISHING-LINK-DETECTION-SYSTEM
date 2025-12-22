import re
from urllib.parse import urlparse
from core.feature_extractor import extract_features


SUSPICIOUS_KEYWORDS = [
    "login", "verify", "bank", "secure",
    "update", "account", "signin", "confirm"
]

URL_SHORTENERS = ["bit.ly", "tinyurl", "t.co", "goo.gl"]

def extract_domain(url):
    try:
        return urlparse(url).netloc.lower()
    except:
        return ""

def is_shortened_url(domain):
    return any(short in domain for short in URL_SHORTENERS)


def analyze_url(url):
    features = extract_features(url)
    score = 0
    reasons = []

    if features["length"] > 75:
        score += 2
        reasons.append("URL is too long")

    if features["has_ip"]:
        score += 3
        reasons.append("Uses IP address instead of domain")

    if not features["has_https"]:
        score += 1
        reasons.append("HTTPS not used")

    if features["dot_count"] > 5:
        score += 1
        reasons.append("Too many subdomains")

    for word in SUSPICIOUS_KEYWORDS:
        if word in url.lower():
            score += 2
            reasons.append(f"Suspicious keyword detected: {word}")

    domain = extract_domain(url)
    if is_shortened_url(domain):
        score += 2
        reasons.append("Shortened URL detected")
    if "@" in url:
        score += 2
        reasons.append("URL contains '@' symbol")
    return score, reasons
