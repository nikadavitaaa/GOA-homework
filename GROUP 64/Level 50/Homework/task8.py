words = ['ant', 'elephant', 'dog', 'giraffe']

# Lambda ფუნქცია, რომელიც აბრუნებს True, თუ სიტყვის სიგრძე >= 5
length_check = lambda word: len(word) >= 5

# filter ფუნქცია
result = list(filter(length_check, words))

print(result)
