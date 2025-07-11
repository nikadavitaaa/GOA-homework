def modify_set(s):
    s.add(1)
    s.add(2)
    s.add(3)
    s.remove(1)
    return s

print(modify_set({4, 5}))
