from core.url_input import get_url
from core.sender_input import get_sender_email
from core.rule_engine import analyze_url
from core.sender_rules import analyze_sender, is_external_sender
from core.decision_engine import classify
from database.db_manager import save_scan
from core.email_content_input import get_email_content
from core.grammar_rules import analyze_grammar
from core.attachment_input import get_attachment_name
from core.attachment_rules import analyze_attachment


def scan_phishing(url, sender_email, email_content, attachment):
    total_score = 0
    reasons = []

    url_score, url_reasons = analyze_url(url)
    total_score += url_score
    reasons.extend(url_reasons)

    sender_score, sender_reasons = analyze_sender(sender_email, email_content)
    total_score += sender_score
    reasons.extend(sender_reasons)

    grammar_score, grammar_reasons = analyze_grammar(email_content)
    total_score += grammar_score
    reasons.extend(grammar_reasons)

    external = is_external_sender(sender_email)

    attach_score, attach_reasons = analyze_attachment(attachment, external)
    total_score += attach_score
    reasons.extend(attach_reasons)

    result = classify(total_score)

    save_scan(sender_email, url, result, total_score, reasons)

    return result, total_score, reasons


def main():
    url = get_url()
    sender_email = get_sender_email()
    email_content = get_email_content()
    attachment = get_attachment_name()

    result, score, reasons = scan_phishing(
        url, sender_email, email_content, attachment
    )

    print("\nResult:", result)
    print("Score:", score)
    print("Reasons:")
    for r in reasons:
        print("-", r)


if __name__ == "__main__":
    main()
