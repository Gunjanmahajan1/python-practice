from datetime import datetime

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def month_name(mon):
    months = ["None", "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"]
    return months[mon]

mon = input("Enter your birth month (as a number): ")
date = int(input("Enter your birth date: "))
year = int(input("Enter your birth year: "))

current_cdate = datetime.now()
current_year = current_cdate.year
current_date = current_cdate.day
current_mon = current_cdate.month

age = current_year - year


if mon == 2:
    if is_leap_year(year) and date <= 29:
        print(f"You will complete age {age} on date {date} of this month.")
    elif not is_leap_year(year) and date <= 28:
        print(f"You will complete age {age} on date {date} of this month.")
    else:
        print("Enter a correct birthdate.")
elif 1 <= mon <= 12 and 1 <= date <= 31:
    if current_mon == mon and current_date == date:
        print(f"You completed {age} today!!!")
    elif current_mon == mon:
        print(f"You will complete age {age} on date {date} of this month.")
    else:
        print(f"You will complete age {age} on date {date} of {month_name(mon)}.")
else:
    print("Enter a correct birthdate.")
    