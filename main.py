from core.url_input import get_url
from core.sender_input import get_sender_email
from core.rule_engine import analyze_url
from core.sender_rules import analyze_sender
from core.decision_engine import classify
from database.db_manager import save_scan
from core.email_content_input import get_email_content
from core.grammar_rules import analyze_grammar
from core.attachment_input import get_attachment_name
from core.attachment_rules import analyze_attachment
from core.sender_rules import is_external_sender




def main():
    url = get_url()
    sender_email = get_sender_email()
    email_content = get_email_content()
    attachment = get_attachment_name()
    url_score, url_reasons = analyze_url(url)

    
    sender_score, sender_reasons = analyze_sender(sender_email, email_content)
    grammar_score, grammar_reasons = analyze_grammar(email_content)
    attach_score, attach_reasons = analyze_attachment(attachment)
    external = is_external_sender(sender_email)
    
    total_score = url_score + sender_score + grammar_score + attach_score
    reasons = url_reasons + sender_reasons + grammar_reasons + attach_reasons


    result = classify(total_score)


    print("\nResult:", result)

    print("Score:", total_score)

    print("Reasons:")

    for r in reasons:

        print("-", r)


    save_scan(sender_email, url, result, total_score, reasons)


if __name__ == "__main__":
    main()

