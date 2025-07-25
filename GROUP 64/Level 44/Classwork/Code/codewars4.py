"https://www.codewars.com/kata/554e4a2f232cdd87d9000038/train/python"

"Complementary DNA"

def DNA_strand(dna):
    second_side = ""
    for acid in dna:
        if acid == "A":
            second_side += "T"
        elif acid == "T":
            second_side += "A"
        elif acid == "G":
            second_side += "C"
        elif acid == "C":
            second_side += "G"
    return second_side