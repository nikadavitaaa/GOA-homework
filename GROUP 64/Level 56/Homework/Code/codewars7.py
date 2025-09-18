"https://www.codewars.com/kata/5412509bd436bd33920011bc/train/python"

"Credit Card Mask"

def maskify(cc):
    return '#' * max(0, len(cc) - 4) + cc[-4:]