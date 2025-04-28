total = 0
count = 0
num = 0

while num != -1:
    num = float(input("შეიყვანეთ რიცხვი (-1-ს შეყვანით შეწყდება): "))
    if num != -1:
        total += num
        count += 1

if count > 0:
    average = total / count
    print("შეყვანილი რიცხვების საშუალო:", average)
else:
    print("არ შეიყვანეთ არანაირი რიცხვი.")
