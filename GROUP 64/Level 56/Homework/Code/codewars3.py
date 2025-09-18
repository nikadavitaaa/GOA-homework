"https://www.codewars.com/kata/576b93db1129fcf2200001e6/train/python"

"Sum without highest and lowest number"

def sum_array(arr):
    if arr is None or len(arr) <= 1:
        return 0
    return sum(arr) - max(arr) - min(arr)
