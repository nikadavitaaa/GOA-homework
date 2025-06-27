"Heron's formula"

"https://www.codewars.com/kata/57aa218e72292d98d500240f/train/python"

import math

def heron(a, b, c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))