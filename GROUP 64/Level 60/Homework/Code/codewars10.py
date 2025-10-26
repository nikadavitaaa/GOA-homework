"https://www.codewars.com/kata/517abf86da9663f1d2000003/train/python"

def to_camel_case(text):
    if not text:
        return text
    text = text.replace('_', '-')
    
    parts = text.split('-')
    
    first = parts[0]
    
    rest = [p.capitalize() for p in parts[1:]]
    
    return first + ''.join(rest)
