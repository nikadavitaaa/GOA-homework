Prods = {
    "Table": 90,
    "Chair": 80,
    "Sofa": 85,
    "Couch": 97
}

Cheap_prods = dict(filter(lambda item: item[1] < 90, Prods.items()))
