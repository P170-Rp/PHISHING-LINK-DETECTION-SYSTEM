import re

def is_valid_url(url):
    return bool(re.match(r'https?://', url))
