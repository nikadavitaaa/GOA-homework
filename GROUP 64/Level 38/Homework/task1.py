def manual_index(lst, element):
    num = 0
    for item in lst:
        if item == element:
            return num
        num += 1
    return -1
