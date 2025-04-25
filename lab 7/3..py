
data = [
    {"dept_no": 101, "roll_no": "E001", "salary": 50000},
    {"dept_no": 102, "roll_no": "E002", "salary": 60000},
    {"dept_no": 101, "roll_no": "E003", "salary": 45000},
    {"dept_no": 103, "roll_no": "E004", "salary": 55000},
    {"dept_no": 102, "roll_no": "E005", "salary": 70000},
    {"dept_no": 103, "roll_no": "E006", "salary": 52000},
]


dept_salaries = {}

for entry in data:
    dept_no = entry["dept_no"]
    salary = entry["salary"]
    if dept_no not in dept_salaries:
        dept_salaries[dept_no] = []
    dept_salaries[dept_no].append(salary)


for dept_no, salaries in dept_salaries.items():
    print(f"Department {dept_no}: Min Salary = {min(salaries)}, Max Salary = {max(salaries)}")

