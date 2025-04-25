def remove_substring(main_string, sub_string):
    return main_string.replace(sub_string, '')


main_string = input("Enter the main string: ")
sub_string = input("Enter the substring to remove: ")


result_string = remove_substring(main_string, sub_string)
print(f"The new string after removing '{sub_string}' is: {result_string}")


