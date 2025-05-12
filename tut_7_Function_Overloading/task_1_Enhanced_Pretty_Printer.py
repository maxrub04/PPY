"""Create a versatile function pretty_print that adapts output based on type:
• int: show whether it's even/odd
• float: display with 2 decimal precision
• str: show length and print it in the reverse order
• dict: display the number of keys and list key-value pairs
• Default: print type and value
🧪 Example usage
pretty_print(8)
pretty_print(3.14159)
pretty_print("Hello World
pretty_print("A very long string example to test the reversal and length handling.")
pretty_print({"x": 1, "y": 2})
pretty_print({"name": "Alice", "age": 30, "city": "Wonderland"""
def pretty_print(value):
    if isinstance(value, int):
        print(f"{value} is {'odd' if value % 2 else 'even'}")
    elif isinstance(value, float):
        print(f"{value:.2f}")
    elif isinstance(value, str):
        print(f"'{value}' length is: {len(value)} , reverse: {value[::-1]}")
    elif isinstance(value, dict):
        print(f"Dict with {len(value)} keys and {len(value.items())} items")
    else:
        print(f"{type(value)}: {value}")
pretty_print(8)
pretty_print(3.14159)
pretty_print("Hello World")
pretty_print("A very long string example to test the reversal and length handling.")
pretty_print({"x": 1, "y": 2})
pretty_print({"name": "Alice", "age": 30, "city": None})
pretty_print(True) # python treats boolean as subclass of int