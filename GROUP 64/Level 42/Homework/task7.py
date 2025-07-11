def modify_dict(dict):
    # ვამატებთ ახალ წყვილს update() მეთოდით
    dict.update({'age': 14})

    # ვშლით ბოლო წყვილს popitem() მეთოდით
    removed_item = dict.popitem()

    print("Removed item:", removed_item)
    print("Dictionary after popping an item:", dict)


student = {
    "name": "Nika", 
    "hobby": "Bjj"}
modify_dict(student)
