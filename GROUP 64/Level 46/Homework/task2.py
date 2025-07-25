words = ['apple', 'banana', 'cat', 'elephant', 'dog', 'grapefruit']
long_words = []
for word in words:
    if len(word) > 5:
        long_words.append(word)

print(long_words)

# -------------------------------------------------------------------

long_words = [word for word in words if len(word) > 5]
print(long_words)  # ['banana', 'elephant', 'grapefruit']

# -------------------------------------------------------------------