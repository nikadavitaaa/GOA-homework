drinks = ["Cola", "Fanta", "Sprite", "Iced Tea", "Lemonade"]

fav = drinks[1]

drink6 = input("შედე ცივი სასმელი მაცივარში: ")

drinks = ["Cola", "Fanta", "Sprite", "Iced Tea", "Lemonade", drink6]

print("სასმელების სია:", drinks)

choice = input("შემოიტანე სასმელის ინდექსი (0-5): ")
choice = int(choice)

print("შენ აირჩიე:", drinks[choice])

name = "ნიკა"

print(name[0], name[2], name[3])
