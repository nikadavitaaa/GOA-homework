fruits = ["ვაშლი", "მსხალი", "ატამი", "ბანანი", "ანანასი", "საზამთრო"]

reversed_fruits = fruits[::-1]

index = 0
for fruit in reversed_fruits:
    if index % 2 == 0:
        print(fruits)
    index = index + 1
