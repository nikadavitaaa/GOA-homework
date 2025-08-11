"https://www.codewars.com/kata/5a00e05cc374cb34d100000d/train/python"

"Reversed sequence"

def reverse_seq(n):
    res = []
    
    for num in range(n, 0, -1):
        res.append(num)
    return res