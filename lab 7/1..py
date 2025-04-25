
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict3 = {"e": 5, "f": 6}


combined_dict = {}
for d in (dict1, dict2, dict3):
    combined_dict.update(d)


print("Combined dictionary:", combined_dict)

