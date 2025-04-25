

import csv


filename = "example.csv"


data = [
    ["Name", "Age", "City"],
    ["Alice", 25, "New York"],
    ["Bob", 30, "London"],
    ["Charlie", 22, "Mumbai"]
]


with open(filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    
    writer.writerows(data)

print(f"CSV file '{filename}' has been created successfully!")



data = [
    ["Name", "Age", "City"],
    ["Alice", 25, "New York"],
    ["Bob", 30, "London"],
    ["Charlie", 22, "Mumbai"]
]


with open(filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

   
    writer.writerows(data)

print(f"CSV file '{filename}' has been created successfully!")


