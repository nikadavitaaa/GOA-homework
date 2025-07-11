animal = {
    "species": "dog",
    "age": 5,
    "color": "brown"
}

print("Original animal dictionary: ", animal)

# ვქმნით animal-ის კოპიოს :D copy() მეთოდით
animal_copy = animal.copy()

# ორივე ლექსიკონის დაცლა clear() მეთოდით
animal.clear()
animal_copy.clear()


print("Original after clearing: ", animal)
print("Copy after clearing: ", animal_copy)