words_list = ["apple", "banana", "cherry", "watermelon", "pear"]

def longest_word(words):
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

print(longest_word(words_list))
