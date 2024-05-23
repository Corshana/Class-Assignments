year = int(input("Enter a year"))

def leap_year():

    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        return True
    else:
        return False
    
    year = int(input("Enter a year"))

    if leap_year(year):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")