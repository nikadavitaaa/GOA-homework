"https://www.codewars.com/kata/545cedaa9943f7fe7b000048/train/python"

"Detect Pangram"

def is_pangram(st):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    st = st.lower()

    for letter in alphabet:
        if letter not in st:
            return False
    return True