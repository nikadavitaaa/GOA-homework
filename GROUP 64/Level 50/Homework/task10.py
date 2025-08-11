nums = [1, 2, 3, 4, 5, 6]

evens = filter(lambda x: x % 2 == 0, nums)

result = map(lambda x: x + 10, evens)

for num in result:
    print(num)
