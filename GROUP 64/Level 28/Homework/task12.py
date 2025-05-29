text = "I visited Georgia, Armenia and Greece"

search_word = input("შეიყვანე საძიებელი სიტყვა: ")

position = text.find(search_word)

if position != -1:
    print("position:", position)
else:
    print("word not found")
