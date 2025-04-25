import pandas as pd
file_path = "student_records.xlsx"  
df = pd.read_excel(file_path)
students_dict = {}
for index, row in df.iterrows():
    roll_no = row['RollNo']
    name = row['Name']
    marks = [row['Subject1'], row['Subject2'], row['Subject3']]
    total_marks = sum(marks)
    
    students_dict[roll_no] = {
        'Name': name,
        'Marks': marks,
        'Total': total_marks
    }
for roll_no, details in students_dict.items():
    print(f"Roll No: {roll_no}, Name: {details['Name']}, Marks: {details['Marks']}, Total: {details['Total']}")

