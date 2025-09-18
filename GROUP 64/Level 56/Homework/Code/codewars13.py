"https://www.codewars.com/kata/541c8630095125aba6000c00/train/python"

"Sum of Digits / Digital Root"

def digital_root(n):
    
    while n > 9:
        total = 0
    
        for digit in str(n):
            total += int(digit)
        n = total
    return n