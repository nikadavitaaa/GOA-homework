numbers = {1, 2, 3, 4, 5}
print(numbers)


# set - ში ამატებს ელემენტებს
numbers.add(6)
numbers.add(7)
print(numbers)

# set - იდან შლის ელემენტებს
numbers.remove(1)
numbers.remove(2)
print("წაშლის შემდეგ:", numbers)


other_numbers = {4, 5, 6, 10}

# Union – აერთიანებს ორივე set-ის ელემენტებს
print("Union:", numbers.union(other_numbers))

# Intersection – აჩვენებს მხოლოდ საერთო ელემენტებს
print("Intersection:", numbers.intersection(other_numbers))

# Difference – აჩვენებს მხოლოდ პირველში არსებულ ელემენტებს, რომლებიც მეორეში არ არის
print("Difference (numbers - other_numbers):", numbers.difference(other_numbers))