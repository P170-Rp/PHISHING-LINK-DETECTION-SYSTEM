# Dangerous attachment extensions
DANGEROUS_EXTENSIONS = [
    ".exe", ".js", ".scr", ".bat",
    ".cmd", ".vbs", ".zip", ".rar",
    ".html", ".iso"
]

def analyze_attachment(attachment_name, sender_is_external=True):
    score = 0
    reasons = []

    if not attachment_name:
        return score, reasons   # No attachment

    attachment = attachment_name.lower()

    for ext in DANGEROUS_EXTENSIONS:
        if attachment.endswith(ext):
            if sender_is_external:
                score += 4
                reasons.append(
                    f"Unexpected dangerous attachment detected: {attachment}"
                )
            else:
                score += 2
                reasons.append(
                    f"Suspicious attachment detected: {attachment}"
                )
            break

    return score, reasons
