''' https://www.codewars.com/kata/546e2562b03326a88e000020/train/python '''

''' Square Every Digit '''

def square_digits(num):
    result = ""
    for char in str(num):
        result += str(int(char) ** 2)
    return int(result)
