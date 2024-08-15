import datetime as dt

def main():
    """
    Asks the user for a date given the day, the month, and the year.
    The program will display the formatted date and the day of the week.
    """
    day = int(input("Key in the day of the month: "))
    month = int(input("Key in the month number (1 = Jan, 2 = Feb, ...): "))
    year = int(input("Key in the year: "))
    
    d = dt.datetime(year, month, day)
    print(f"{d:%d} {d:%B} {year} is a {d:%A}")

if __name__ == "__main__":
    main()