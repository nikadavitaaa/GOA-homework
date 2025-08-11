"https://www.codewars.com/kata/57eae65a4321032ce000002d/train/python"

"Fake Binary"

def fake_bin(x):
    res = ""
    
    for digit in x:
        if int(digit) < 5:
            res += "0"
        else:
            res += "1"
            
    return res