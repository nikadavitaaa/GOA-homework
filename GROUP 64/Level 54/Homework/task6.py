import time

def decorator(func):
    def wrapper():
        print("ფუნქცია დაიწყო")
        start_time = time.time()
        func()
        time_end = time.time()
        duration = time_end - start_time 
        print(f"ფუნქციამ იმუშავა {duration:.4f} წამი")
    return wrapper

@decorator
def greet():
    print("Hello world")
greet()
