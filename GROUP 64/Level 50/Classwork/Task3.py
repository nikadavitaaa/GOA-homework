# lambda - ეს არის ერთ ხაზიანი ფუნქცია, რომელიც, აადვილებს და ამოკლებს კოდს. 

numbers = [1, 2, 3, 4, 5, 6]

squares = list(map(lambda x: x ** 2, numbers))

# filter ინახავს მხოლოდ იმ ელემენტებს, რომლებზეც ფუნქცია აბრუნებს True-ს.
even = list(filter(lambda x: x % 2 == 0, numbers))

print("Original:", numbers)
print("Squares:", squares)
print("Even numbers:", even)



#                 MANUAL FUNCTIONS

def manual_map(func, iterable):
    result = []
    for item in iterable:
        result.append(func(item))
    return result

# -------------------------------------

def manual_filter(func, iterable):
    result = []
    for item in iterable:
        if func(item):
            result.append(item)
    return result
