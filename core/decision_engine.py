def classify(score):
    if score <= 2:
        return "SAFE"
    elif score <= 5:
        return "SUSPICIOUS"
    else:
        return "HIGH RISK"
