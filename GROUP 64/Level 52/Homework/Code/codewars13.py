"https://www.codewars.com/kata/546f922b54af40e1e90001da/train/python"

"Replace With Alphabet Position"

def alphabet_position(text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    res = []
    
    for char in text.lower():
        if char in alphabet:
            position = alphabet.index(char) + 1
            res.append(str(position))
    
    return " ".join(res)