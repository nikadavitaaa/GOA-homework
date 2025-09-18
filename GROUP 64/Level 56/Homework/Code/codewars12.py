"https://www.codewars.com/kata/5680781b6b7c2be860000036/train/python"

"Find the vowels"

def vowel_indices(word):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']

    positions = []


    for i in range(len(word)):
        if word[i] in vowels:
            positions.append(i + 1)

    return positions