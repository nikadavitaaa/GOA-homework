"https://www.codewars.com/kata/54da5a58ea159efa38000836/train/python"

def find_it(seq):
    for x in set(seq):
        if seq.count(x) % 2 == 1:
            return x
