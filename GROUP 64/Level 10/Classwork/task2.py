'''მომხმარებელს შემოატანინეთ თავისი სიმაღლე, შემდეგ შემოატანინეთ წლების რაოდენობა, მიღებული ინფორმაცია შეინახეთ ცვლადებში და გამოუთვალეთ მომხმარებელს სავაურდო სიმაღლე EH (Estimated Height) როდესაც გავა y წელი (რაც მომხმარებლმა შემოიტანა) თუ დაუშვათ ყოველ წელს სიმაღლე იზრდება 0.5-ით. საბოლოოდ გამოუტანეთ EH'''

height = input("enter your height: ")

height = float(height)

age = int(input("enter your age: "))

height = height + (age * 0.5)

print(height)

