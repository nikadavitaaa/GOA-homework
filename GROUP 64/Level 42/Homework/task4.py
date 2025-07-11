def get_keys_and_values(dict):
    # ვიღებთ ლექსიკონის ყველა "გასაღებს" keys() მეთოდით
    keys = dict.keys()

    # ვიღებთ ლექსიკონის ყველა მნიშვნელობას values() მეთოდით
    values = dict.values()

    print(f'Keys = {keys}')
    print(f'velues = {values}')

    return keys, values


sample_dict = {
    "name": "Nika",
    "age": 30,
    "city": "Tbilisi"
}

keys, values = get_keys_and_values(sample_dict)
