"https://www.codewars.com/kata/525f50e3b73515a6db000b83/train/python"

"Create Phone Number"

def create_phone_number(n):
    s = ''.join(map(str, n))
    return f"({s[0:3]}) {s[3:6]}-{s[6:10]}"