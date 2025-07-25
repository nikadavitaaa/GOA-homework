animals = ['tiger', 'lion', 'zebra', 'elephant', 'giraffe']

first_letters = []
for word in animals:
    first_letters.append(word[0])

print(first_letters)

#------------------------------------------------------------

first_letters = [word[0] for word in animals]
print(first_letters)

#------------------------------------------------------------

e_words = [word for word in animals if word.startswith('e')]
print(e_words)

#------------------------------------------------------------