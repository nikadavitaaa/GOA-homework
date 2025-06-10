def calc_fact(n):
    result = 1
    for num in range(1, n + 1):
        result = result * num
    return result

print(calc_fact(5))