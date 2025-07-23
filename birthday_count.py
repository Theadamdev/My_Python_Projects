import datetime
today = datetime.date.today()
month : int = today.month
day : int = today.day
birth_month = int(input("Enter your birth month (1 to 12): "))
birth_day = int(input("Enter your birth day (1 to 31): "))
birthday = datetime.date(today.year, birth_month, birth_day)
if birthday < today :
    print("Your birthday has passed")
else :
    days_left : int = (birthday-today).days
    print(f"Your birthday is in {days_left} days")
    if days_left == 0 :
        print("I hope you\'re fasting today")
