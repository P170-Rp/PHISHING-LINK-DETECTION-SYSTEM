from core.url_input import get_url

from core.sender_input import get_sender_email

from core.rule_engine import analyze_url

from core.sender_rules import analyze_sender

from core.decision_engine import classify

from database.db_manager import save_scan

from core.email_content_input import get_email_content

from core.grammar_rules import analyze_grammar



def main():
    url = get_url()
    sender_email = get_sender_email()
    email_content = get_email_content()
    url_score, url_reasons = analyze_url(url)

    
    sender_score, sender_reasons = analyze_sender(sender_email, email_content)
    grammar_score, grammar_reasons = analyze_grammar(email_content)


    total_score = url_score + sender_score + grammar_score
    reasons = url_reasons + sender_reasons + grammar_reasons


    result = classify(total_score)


    print("\nResult:", result)

    print("Score:", total_score)

    print("Reasons:")

    for r in reasons:

        print("-", r)


    save_scan(sender_email, url, result, total_score, reasons)


if __name__ == "__main__":
    main()

