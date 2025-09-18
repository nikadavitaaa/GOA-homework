def decorator(func):
    def wrapper():
        print("Started")
        func()
        print("Ended")
    return wrapper

@decorator
def greet():
    print("Hello world")
