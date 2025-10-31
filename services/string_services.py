import re

def extract_braced_strings(sentence: str):
    return re.findall(r'\{[^}]+\}', sentence)

def replace_placeholder(sentence: str, placeholder: str, value: str):
    return sentence.replace(placeholder, value)