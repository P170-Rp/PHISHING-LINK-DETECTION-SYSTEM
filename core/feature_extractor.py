import re

def extract_features(url):
    return {
        "length": len(url),
        "has_https": url.startswith("https"),
        "has_ip": bool(re.search(r'\d+\.\d+\.\d+\.\d+', url)),
        "dot_count": url.count('.')
    }
