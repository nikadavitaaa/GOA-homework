#      პირველი


try:
    age_input = input("Enter your age: ")
    age = int(age_input)

    if age < 0:
        raise ValueError("Age cant be less than zero")

    print("Your age:", age)

except ValueError:
    print("Error:", ValueError)




#         მეორე



try:
    word = input("Enter a word (at least 5 characters): ")
    
    if len(word) < 5:
        raise ValueError("The word is too short!")
    print("Your word is:", word)

except ValueError as error:
    print("Error:", error)
