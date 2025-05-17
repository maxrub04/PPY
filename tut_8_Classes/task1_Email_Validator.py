"""Email Validator
Objective:
Create a regular expression that validates email addresses in the following format:
    • The email must start with a sequence of alphanumeric characters or underscores.
    • Then, there must be a "@" symbol.
    • After the "@" symbol, there should be a domain name, which can consist of
    alphanumeric characters or hyphens.
    • Finally, there must be a period (.) followed by a domain extension, which is between
2 and 6 alphabetic characters (e.g., .com, .org).
Instructions:
1. Write a regular expression that matches valid email addresses according to the above format.
2. Using Python's re module, write a function validate_email(email) that:
    -Takes an email string as input.
    -Returns True if the email is valid, and False otherwise"""
import re
def validate_email(email):
    pattern = re.compile(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,6}$")
    return bool(pattern.match(email))

print(validate_email("maksrub04@gmail.com"))  # True
print(validate_email("user@example-domain.com"))  # True
print(validate_email("maksrub04gmail.com"))  # False
print(validate_email("maksrub04@gmailcom")) # False


