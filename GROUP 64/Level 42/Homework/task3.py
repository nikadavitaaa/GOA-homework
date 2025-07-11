student = {
    "Name": "Nika",
    "Hobby": "Bjj",
    "Height": 280,
    "Weight": 75
}


# .get() — იღებს მნიშვნელობას ლექსიკონიდან
name = student.get("Name")
print(f'Name = {name}')

#.pop() — შლის ელემენტს და აბრუნებს მის მნიშვნელობას
height_value = student.pop("Height")
print("Removed height:", height_value)