# Disemvowel Trolls

"https://www.codewars.com/kata/52fba66badcd10859f00097e/train/python"

def disemvowel(string): 
    vowels = "aeiouAEIOU"
    result = ""
    
    for char in string:
        if char not in vowels:
            result += char
    
    return result