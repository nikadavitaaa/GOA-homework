def tuple_info(tuple):
    print(len(tuple))
    if len(tuple) > 0:
        print(tuple[0] , tuple[-1])
    else:
        print("tuple is empty")

tup1 = [1, 3, 2, 5, 8, 90]

tuple_info(tup1)