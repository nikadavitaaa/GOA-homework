person = {
    "name": "Nika",
    "hobby": "BJJ",
    "Height": 2.20,
    "weight": 75,
}

# 1. get() — აბრუნებს გასაღების მნიშვნელობას
print(person.get("name"))
print(person.get("age"))

# 2. keys() — აბრუნებს ყველა key-ს
print(person.keys())

# 3. values() — აბრუნებს ყველა მნიშვნელობას (Nika, BJJ...)
print(person.values())

# 4. items() — აბრუნებს ყველა წყვილს (key, value)
print(person.items())

# 5. update() — ან ანახლებთ მნიშვნელობას, ან ამატებთ ახალს
person.update({"weight": 70})
person.update({"age": 25})

# 6. pop() — შლის მითითებულ key-ს და აბრუნებს მის მნიშვნელობას
removed = person.pop("hobby")
print(removed)

# 7. clear() — მთლიანად ცლის ლექსიკონს

