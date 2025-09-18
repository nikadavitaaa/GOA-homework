"https://www.codewars.com/kata/563cf89eb4747c5fb100001b/train/python"

"Remove the minimum"

def remove_smallest(numbers):
    
    if numbers == []:
        return []
    
    smallest = min(numbers)
    lowest_index = numbers.index(smallest)
    
    new_list = []
    for num in numbers:
        new_list.append(num)
    new_list.pop(lowest_index)
    return new_list