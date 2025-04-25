def to_lowercase(s):
    return s.lower()

def to_uppercase(s):
    return s.upper()

def to_togglecase(s):
    return ''.join([char.lower() if char.isupper() else char.upper() for char in s])


user_string = input("Enter a string: ")


lowercase_string = to_lowercase(user_string)
uppercase_string = to_uppercase(user_string)
togglecase_string = to_togglecase(user_string)

print(f"Lowercase: {lowercase_string}")
print(f"Uppercase: {uppercase_string}")
print(f"Toggle case: {togglecase_string}")


