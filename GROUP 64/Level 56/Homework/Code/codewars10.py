"https://www.codewars.com/kata/539ee3b6757843632d00026b/train/python"

"Find the capitals"

def capitals(word):
    result = []
    for i in range(len(word)):
        if word[i].isupper():
            result.append(i)
    return result