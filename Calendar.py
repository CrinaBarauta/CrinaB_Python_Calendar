
import datetime

def days_in_month(year, month):
    """
    Inputs:
      year  - an integer between datetime.MINYEAR and datetime.MAXYEAR
              representing the year
      month - an integer between 1 and 12 representing the month

    Returns:
      The number of days in the input month.
    """
    if datetime.MINYEAR<=year<=datetime.MAXYEAR and 1<=month<12:
        date1=datetime.date(year,month,1)
        next_month=month+1
        date2=datetime.date(year,next_month,1)
        diff=date2-date1
        return diff.days 
    elif datetime.MINYEAR<=year<=datetime.MAXYEAR and month==12:
        return 31
    else:
        return 0

def is_valid_date(year, month, day):
    """
    Inputs:
      year  - an integer representing the year
      month - an integer representing the month
      day   - an integer representing the day

    Returns:
      True if year-month-day is a valid date and
      False otherwise
    """
    if datetime.MINYEAR<=year<=datetime.MAXYEAR and 1<=month<=12 and 1<=day<=days_in_month(year, month):
        return True
    else:
        return False

def days_between(year1, month1, day1, year2, month2, day2):
    """
    Inputs:
      year1  - an integer representing the year of the first date
      month1 - an integer representing the month of the first date
      day1   - an integer representing the day of the first date
      year2  - an integer representing the year of the second date
      month2 - an integer representing the month of the second date
      day2   - an integer representing the day of the second date

    Returns:
      The number of days from the first date to the second date.
      Returns 0 if either date is invalid or the second date is
      before the first date.
    """
    if is_valid_date(year1, month1, day1)==True and is_valid_date(year2, month2, day2)==True:
        date_1= datetime.date(year1,month1,day1)
        date_2= datetime.date(year2,month2,day2)
        diff_nr=date_2 - date_1
        if date_1 < date_2:
            return diff_nr.days
        else:
            return 0
    else:
        return 0

def age_in_days(year, month, day):
    """
    Inputs:
      year  - an integer representing the birthday year
      month - an integer representing the birthday month
      day   - an integer representing the birthday day

    Returns:
      The age of a person with the input birthday as of today.
      Returns 0 if the input date is invalid or if the input
      date is in the future.
    """
    today=datetime.date.today()
    if is_valid_date(year,month,day)==True:
        birth_day=datetime.date(year,month,day)
        if today > birth_day:
            age= days_between(year, month, day, today.year,today.month,today.day)
            return age
        else:
            return 0
    else:
        return 0

print("Find out how many days are in a month of a specific year: ")
days_in_month_year=int(input("Specify the year: "))
days_in_month_month=int(input("Specify a number between 1 and 12 representing the month: "))
print("The number of days in the input month is: ",days_in_month(days_in_month_year, days_in_month_month))
print()
print("Find out how many days are between two dates: ")
days_between_year1=int(input("Specify the year of the first date: "))
days_between_month1=int(input("Specify the month (integer between 1 and 12) of the first date: "))
days_between_day1=int(input("Specify the day of the first date: "))
days_between_year2=int(input("Specify the year of the second date: "))
days_between_month2=int(input("Specify the month (integer between 1 and 12) of the second date: "))
days_between_day2=int(input("Specify the day of the second date: "))
print("Between the two dates are ",days_between(days_between_year1, days_between_month1, days_between_day1, days_between_year2, days_between_month2, days_between_day2))
print()
print("Discover your age in days: ")
age_in_days_year=int(input("Specify your birthday year: "))
age_in_days_month=int(input("Specify your birthday month (integer between 1 and 12): "))
age_in_days_day=int(input("Specify your birthday day: "))
print("You are ",age_in_days(age_in_days_year, age_in_days_month, age_in_days_day)," days old.")