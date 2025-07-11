numbers = set()

# ვამატებ ორ ელემენტს set-ში add() მეთოდით
numbers.add(2)
numbers.add(4)

# ვშლი ორ ელემენტს remove() მეთოდით
numbers.remove(2)
numbers.remove(4)





even_numbers = {2, 4, 6, 8}
numbers = {4, 6, 10}

# ცაერთიანებ ორივე set-ს
union_set = numbers.union(even_numbers)
print("Union:", union_set)


# დავტოვე მხოლოდ ის ელემენტები რომლებიც ორივე set-ში იყო
intersection_set = numbers.intersection(even_numbers)
print("Intersection:", intersection_set)

# გამოვიტანე მხოლოდ ის რიცხვები რომლებიც იტო numbers-ში მაგრამ არა even_numbers-ში
difference_set = numbers.difference(even_numbers)
print("Difference:", difference_set)
