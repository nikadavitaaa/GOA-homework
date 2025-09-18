"https://www.codewars.com/kata/54ff0d1f355cfd20e60001fc/train/python"

"Factorial"

def factorial(n):
    if n < 0 or n > 12:
        raise ValueError
    
    if n == 0:
        return 1
    
    product = 1
    for num in range(2, n + 1):
        product *= num
    return product