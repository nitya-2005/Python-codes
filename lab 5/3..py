from datetime import date

def calculate_days_between_dates(date1, date2):
   
    d1 = date(date1[2], date1[1], date1[0])  
    d2 = date(date2[2], date2[1], date2[0])
    
    
    difference = abs((d2 - d1).days)
    return difference


date1 = (10, 3, 2025)  
date2 = (17, 3, 2025)

days_between = calculate_days_between_dates(date1, date2)

print(f"Number of days between {date1} and {date2}: {days_between}")

