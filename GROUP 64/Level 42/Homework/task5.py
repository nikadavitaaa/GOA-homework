person = {
    "name": "Nika",
    "age": 30,
    "city": "Tbilisi"
}

# .items() მეთოდი აბრუნებს ლექსიკონის key და value წყვილებს tuple-ებად
for key, value in person.items():
    print(f'{key}: {value}')
