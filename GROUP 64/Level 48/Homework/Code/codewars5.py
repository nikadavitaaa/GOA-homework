"https://www.codewars.com/kata/5b077ebdaf15be5c7f000077/train/python"

"If you can't sleep, just count sheep!!"

def count_sheep(n):
    res = ""
    
    for i in range(1, n + 1):
        res += f"{i} sheep..."
    return res