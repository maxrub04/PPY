from functools import wraps

def log(level):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"{level}: Starting {func.__name__}")
            result = func(*args, **kwargs)
            print(f"{level}: Finished {func.__name__}\n")
            return result
        return wrapper
    return decorator


@log("INFO")
def process_data():
    print("Processing data...")

@log("DEBUG")
def calculate_sum(a, b):
    print(f"Calculating sum of {a} and {b}...")
    return a + b
@log("WARNING")
def warning():
    print("Warning!")

process_data()
calculate_sum(2, 3)
warning()
result = calculate_sum(2, 3)
print(f"Result: {result}")