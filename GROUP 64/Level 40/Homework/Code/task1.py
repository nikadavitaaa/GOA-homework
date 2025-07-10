# --- Split ---

txt = "dog, cat, cow"
print(txt.split())

scentence = "hello world"
print(scentence.split())

Name_Age = "Nika, 15"
print(Name_Age.split())

# --- Join ---

words = ["one", "two", "three"]
print("space".join(words))

letters = ["A", "B", "C", "D", "E"]
print("-".join(letters))

Nums = ["one", "two", "three", "four", "five"]
print("to".join(Nums))

# --- Strip ---

text = "    Hello    "
print(text.strip())

gibberish_banana = "ffgs, banana gtsd"
print(gibberish_banana.strip("fgstd, "))

date = "May-fifth-nineteen-ninety    ghj"
print(date.strip("ghj "))

# --- Replace ---

text = "I like apples"
print(text.replace("apples", "kiwis"))

Email = "exampleat.com"
print(Email.replace("at", "@"))

Code = "Hello guys"
print(Code.replace("guys", "World"))