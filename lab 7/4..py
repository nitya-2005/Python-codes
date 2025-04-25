
user_input = input("Enter a string: ")


char_frequency = {}


for char in user_input:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1


print("Character Frequency Dictionary:")
for char, frequency in char_frequency.items():
    print(f"'{char}': {frequency}")

