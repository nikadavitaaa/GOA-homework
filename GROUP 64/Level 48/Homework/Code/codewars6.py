"https://www.codewars.com/kata/57a0885cbb9944e24c00008e/train/python"

"Remove exclamation marks"

def remove_exclamation_marks(s):
    res = ""
    
    for i in s:
        if i != "!":
            res += i
    return res