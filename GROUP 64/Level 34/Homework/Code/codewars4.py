''' Sum Of Positive '''

''' https://www.codewars.com/kata/5715eaedb436cf5606000381/train/python '''

def positive_sum(arr):
    sum = 0
    for numbers in arr:
        if numbers > 0:
            sum += numbers
    return sum