from datetime import datetime, date
d1 = datetime.strptime(input("Enter first date (dd-mm-yyyy): "), "%d-%m-%Y").date()
d2 = datetime.strptime(input("Enter second date (dd-mm-yyyy): "), "%d-%m-%Y").date()
print("Days between:", abs((d2 - d1).days))
print("Day of week for first date:", d1.strftime("%A"))
now = datetime.now()
print("Current date/time:", now.strftime("%d-%m-%Y %H:%M:%S"))
birth = datetime.strptime(input("Enter birth date (dd-mm-yyyy): "), "%d-%m-%Y").date()
today = date.today()
years = today.year - birth.year
months = today.month - birth.month
days = today.day - birth.day
if days < 0:
    months -= 1
    prev_month = (today.month - 1) or 12
    prev_year = today.year if today.month > 1 else today.year - 1
    days += (date(prev_year, prev_month + 1, 1) - date(prev_year, prev_month, 1)).days
if months < 0:
    years -= 1
    months += 12
print(f"Age: {years} years {months} months {days} days")
