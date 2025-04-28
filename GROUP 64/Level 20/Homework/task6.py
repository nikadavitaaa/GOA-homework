sum = 0  
count = 0

number = 0

while number != -1:
    number = int(input("შეიყვანეთ რიცხვი: "))
    
    if number != -1:
        sum += number
        count += 1

if count > 0:
    average = sum / count
    print(f"შეყვანილი რიცხვების საშუალო: {average}")
else:
    print("არ არის შეყვანილი რიცხვი.")
