# მაღალი იერარქიის ფუნქცია არის ისეთი ფუნქცია რომელიც არგუმენტად იღებს კიდევ სხვა ფუნქციას

def apply_function(f, value):
    return f(value)

def square(x):
    return x * x

result = apply_function(square, 5)
print(result)


# წმინდა ფუნქცია ყოველთვის ერთსა და იმავე არგუმენტებზე აბრუნებს ერთსა და იმავე შედეგს, ანუ ის არ არის დამოკიდებული გარე ფაქტორებზე 

def add(a, b):
    return a + b


# არაწმინდა ფუნქციამ შეიძლება გამოიწვიოს გვერდითი ეფექტები, და ის ასევე დამოკიდებულია გარე ფაქტორებზე

counter = 0

def c_ounter():
    global counter
    counter += 1

c_ounter()
print(counter)