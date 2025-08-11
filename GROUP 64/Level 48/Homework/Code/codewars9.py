"https://www.codewars.com/kata/578553c3a1b8d5c40300037c/train/python"

"Ones and Zeros"

def binary_array_to_number(arr):
    b_s = ""
    
    for i in arr:
        b_s += str(i)
        
    return int(b_s, 2)