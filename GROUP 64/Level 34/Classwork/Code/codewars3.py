# Vovel count

"https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/python"

def get_count(sentence):
    attend = 0
    vovels="aeiouAEIOU"
    for char in sentence:
        if char in vovels:
            attend += 1
    return attend