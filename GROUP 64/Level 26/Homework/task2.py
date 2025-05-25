# ხილის სია (კალათა)
basket = ["ვაშლი", "ბანანი", "ფორთოხალი", "მარწყვი", "ატამი"]

# მომხმარებლის საყვარელი ხილი
favorite_fruit = input("შეიყვანეთ თქვენი საყვარელი ხილი: ")

# ცვლადი რომელიც გვეუბნება არის თუ არა ხილი კალათაში
fruit_in_basket = False

# ვამოწმებთ თითოეულ ხილს კალათაში
for fruit in basket:
    if fruit == favorite_fruit:
        fruit_in_basket = True

# ვამოწმებთ შედეგს
if fruit_in_basket:
    print("Good choice")
else:
    print("Fruit not in basket")
