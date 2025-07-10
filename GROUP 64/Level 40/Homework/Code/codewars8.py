"https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9/train/python"

"Shortest Word"

def find_short(s):
    words = s.split()
    shortest_variable = len(words[0])
    
    for i in words[1:]:
        lenght = len(i)
        if lenght < shortest_variable:
            shortest_variable = lenght
            
    return shortest_variable