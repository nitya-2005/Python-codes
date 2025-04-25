
names = {"Alice", "Bob", "Angela", "Brandon", "Amy", "Brian"}


names_with_a = {name for name in names if name.startswith("A")}
names_with_b = {name for name in names if name.startswith("B")}


print("Names starting with 'A':", names_with_a)
print("Names starting with 'B':", names_with_b)

