

numbers = [1, 4, 7, 10, 13, 16, 19]
new_list = []
for num in numbers:
    if num % 2 != 0:
        new_list.append(num * 2)

print(new_list)


# ---------------------------------------------------------

new_list = [num * 2 for num in numbers if num % 2 != 0]
print(new_list)


# -----------------------------------------------------

new_list = [num * 2 for num in numbers]
print(new_list)


# -----------------------------------------------------

new_list = [num for num in numbers if num % 2 == 0]
print(new_list)
