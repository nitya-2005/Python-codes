
my_tuple = (1, 2, 3, 4, 5)


temp_list = list(my_tuple)


temp_list.remove(3)


modified_tuple = tuple(temp_list)

print("Original tuple:", my_tuple)
print("Modified tuple:", modified_tuple)

