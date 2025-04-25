def is_substring(str1, str2):
    return str1 in str2


string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")


if is_substring(string1, string2):
    print(f'"{string1}" is found in "{string2}".')
else:
    print(f'"{string1}" is NOT found in "{string2}".')


if is_substring(string2, string1):
    print(f'"{string2}" is found in "{string1}".')
else:
    print(f'"{string2}" is NOT found in "{string1}".')


