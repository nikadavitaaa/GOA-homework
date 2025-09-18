"https://www.codewars.com/kata/5259b20d6021e9e14c0010d4/train/python"

"Reverse words"

def reverse_words(text):
    words = text.split(" ")
    reversed_words = []
    for word in words:
        reversed_words.append(word[::-1])
    return " ".join(reversed_words)