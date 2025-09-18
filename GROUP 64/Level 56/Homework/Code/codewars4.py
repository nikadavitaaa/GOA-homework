"https://www.codewars.com/kata/576b93db1129fcf2200001e6/train/python"

"Double Char"

def double_char(s):
    result = ""
    for i in s:
        result += i + i
        s.lower()
    return result