from core.url_input import get_url
from core.rule_engine import analyze_url
from core.decision_engine import classify
from database.db_manager import save_scan

def main():
    url = get_url()
    score, reasons = analyze_url(url)
    result = classify(score)

    print("\nResult:", result)
    print("Score:", score)
    print("Reasons:")
    for r in reasons:
        print("-", r)

    save_scan(url, result, score, reasons)

if __name__ == "__main__":
    main()
