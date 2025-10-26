"https://www.codewars.com/kata/5264d2b162488dc400000001/train/python"

def spin_words(sentence):
    words = sentence.split()
    result = [
        word[::-1] if len(word) >= 5 else word
        for word in words
    ]
    return " ".join(result)
