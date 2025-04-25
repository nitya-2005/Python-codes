def count_alphabets_and_digits(s):
    alphabets = 0
    digits = 0

    for char in s:
        if char.isalpha():
            alphabets += 1
        elif char.isdigit():
            digits += 1

    return alphabets, digits


input_string = "Hello123"
alphabets_count, digits_count = count_alphabets_and_digits(input_string)
print(f"Number of alphabets: {alphabets_count}")
print(f"Number of digits: {digits_count}")


