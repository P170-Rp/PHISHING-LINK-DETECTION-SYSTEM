from core.rule_engine import analyze_url

urls = [
    "https://google.com",
    "http://login-bank.com",
    "http://192.168.1.1/login"
]

for url in urls:
    score, reasons = analyze_url(url)
    print(url, score, reasons)
