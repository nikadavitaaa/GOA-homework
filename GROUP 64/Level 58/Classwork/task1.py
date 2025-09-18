# Scope - არის ჩვლადის ხელმისაწვდომoბის "არეალი"

x = 10

def test():
    print(x)

test()
print(x)


def test():
    y = 5
    print(y)

test()

def outer():
    z = 20
    def inner():
        print(z)
    inner()
outer()

