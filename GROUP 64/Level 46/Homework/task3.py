nums = list(range(1, 21))
squares = []
for num in nums:
    squares.append(num ** 2)

print(squares)

#---------------------------------------

squares = [num ** 2 for num in nums]
print(squares)

#---------------------------------------

triples = []
for num in nums:
    triples.append(num * 3)

print(triples)

#---------------------------------------

triples = [num * 3 for num in nums]
print(triples)

#---------------------------------------