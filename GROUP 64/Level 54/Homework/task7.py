def Multiply(*Nums):
    sum = 2
    for num in Nums:
        sum *= num
    return sum

print(Multiply(1,2,3,4,5,6,7))