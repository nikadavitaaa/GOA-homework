"https://www.codewars.com/kata/55cbd4ba903825f7970000f5/train/python"

"Grasshopper - Grade book"

def get_grade(s1, s2, s3):
    
    average = (s1 + s2 + s3) / 3
    
    grades = {
        90: "A",
        80: "B",
        70: "C",
        60: "D",
        0: "F"
    }
    
    for key in grades:
        if average >= key:
            return grades[key]