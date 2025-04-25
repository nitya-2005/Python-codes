def separate_student_details(student_list):
    roll_numbers = []
    names = []
    ages = []
    
    for student in student_list:
        roll_numbers.append(student[0])
        names.append(student[1])
        ages.append(student[2])
    
    return roll_numbers, names, ages


students = [(1, "Alice", 20), (2, "Bob", 21), (3, "Charlie", 19)]
roll_numbers, names, ages = separate_student_details(students)

print("Roll Numbers:", roll_numbers)
print("Names:", names)
print("Ages:", ages)

