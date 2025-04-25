def remove_empty_tuples(input_list):
   
    return [tup for tup in input_list if tup]


tuples_list = [(), ("apple", 50), (), ("banana", 30), (), ("cherry", 40)]
filtered_list = remove_empty_tuples(tuples_list)

print("List after removing empty tuples:", filtered_list)

