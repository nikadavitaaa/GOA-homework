def lst(list):
    unique_items = []
    for i in list:
        if i not in unique_items:
            unique_items.append(i)
            count = [list.count(i)]
            print(f"{i} - {count}")

lst(["apple", "banana", "apple", "kiwi", "orange", "kiwi"])
