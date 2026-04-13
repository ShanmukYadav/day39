import re

def clean_text(text):
    try:
        text = text.lower()
        text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
        return text
    except Exception as e:
        return ""

def handle_negation(text):
    return text.replace("not bad", "good")

def handle_code_mixing(text):
    # simple heuristic
    return text.replace("accha", "good").replace("bahut", "very")

def preprocess_pipeline(text):
    text = clean_text(text)
    text = handle_negation(text)
    text = handle_code_mixing(text)
    return text
