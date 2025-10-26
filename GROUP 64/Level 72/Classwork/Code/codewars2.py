"https://www.codewars.com/kata/581e014b55f2c52bb00000f8/train/python"

def decipher_this(text):
    words = text.split()
    result = []
    
    for word in words:
        num = ''
        i = 0
        
        while i < len(word) and word[i].isdigit():
            num += word[i]
            i += 1
        
        num = int(num)
        chars = word[i:]
        
        if len(chars) > 1:
            chars = chars[-1] + chars[1:-1] + chars[0]
        result.append(chr(num) + chars)
    
    return ' '.join(result)
