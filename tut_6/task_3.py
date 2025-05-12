import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        duration = end - start
        print(f"{func.__name__} took {duration:.4f} seconds to run.")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(2)
    print("Function complete!")

@timer
def multiply(a, b):
    return a * b

slow_function()
print("Result:", multiply(6, 7))
