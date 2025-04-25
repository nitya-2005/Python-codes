def format_hour(hour):
    if hour == 0:
        return "12 AM (Midnight)"
    elif hour == 12:
        return "12 PM (Noon)"
    elif hour < 12:
        return f"{hour} AM"
    else:
        return f"{hour - 12} PM"


for hour in range(24):
    print(format_hour(hour))

