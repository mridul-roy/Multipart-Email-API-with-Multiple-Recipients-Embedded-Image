ALLOWED_DOMAINS = ['gmail.com', 'hotmail.com', 'yahoo.com']
ALLOWED_EMAILS = ['careers@accelx.net']

def is_valid_recipient(email):
    domain = email.split('@')[-1]
    return email in ALLOWED_EMAILS or domain in ALLOWED_DOMAINS
