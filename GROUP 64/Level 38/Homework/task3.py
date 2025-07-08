fruits = ['apple', 'banana', 'orange', 'tangerine', 'kiwi', 'orange']
colors = ['red', 'blue', 'green', 'black', 'yellow', 'blue']
numbers = [5, 3, 8, 1, 0, 9, 3, 5]


# --- fruits ---

# აბრუნებს ელემენტის პირველ ინდექსს
print(fruits.index('apple'))

# ითვლის რამდენჯერ გვხვდება 'apple'
print(fruits.count('apple'))

# ანბანის მიხედვით აწყობს სიას
fruits.sort()
print(fruits)

# sorted - ქმნის ახალ დალაგებულ სიას
fruits.sort()
print(fruits)

# მინიმალური ელემენტი ალფბეთის მიხედვით
print(min(fruits))

# მაქსიმალური ელემენტი ალფბეთის მიხედვით
print(max(fruits))


# --- colors ---

# აბრუნებს კონკრეტული ელემენტის პირველ ინდექსს
print(colors.index('blue'))

# რამდენჯერ არის 'blue' სიაში
print(colors.count('blue'))

# აწყობს სიას ალფბეთურად
colors.sort()
print(colors)

# sorted - ქმნის ახალ დალაგებულ ვერსიას
print(sorted(colors))

# აბრუნებს მოკლე ელემენტს
print(min(colors))

# აბრუნებს უგრძეს ელემენტს
print(max(colors))


# --- numbers ---

# აბრუნებს ინდექსს, რომელზეც პირველად გვხვდება 5
print(numbers.index(5))

# ითვლის რამდენჯერ არის 5 სიაში
print(numbers.count(5))

# აწყობს სიას ზრდადობით
numbers.sort()
print(numbers)

# sorted - ქმნის ახალ დალაგებულ სიას
print(sorted(numbers))

# მინიმალური რიცხვი
print(min(numbers))

# მაქსიმალური რიცხვი
print(max(numbers))
