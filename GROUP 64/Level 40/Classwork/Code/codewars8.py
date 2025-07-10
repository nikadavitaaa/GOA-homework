"https://www.codewars.com/kata/53dbd5315a3c69eed20002dd/train/python"

"Training on List Filtering"

def filter_list(l):
    filtered_list = []
    for element in l:
        if type(element) == type(1):
            filtered_list.append(element)
    return filtered_list
