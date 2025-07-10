"https://www.codewars.com/kata/54ba84be607a92aa900000f1/train/python"

"Isograms"

def is_isogram(string):
    string = string.lower()
    seen = []
    
    for i in string:
        if i in seen:
            return False
        seen.append(i)
    return True