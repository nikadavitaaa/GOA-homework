'''2) მომხმარებელს შემოატანინეთ 2 რიცხვი, შემდეგ კი პირველი რიცხვიდან მეორეს ჩათვლით არსებული ყველა რიცხვი დაბეჭდეთ'''


num1 = int(input("enter the first num: "))
num2 = int(input("enter the second num: "))

for number in range(num1, num2 + 1):
    print(number)