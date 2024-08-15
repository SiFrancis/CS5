import datetime as dt

def main():
    """
    Asks the user for a date given the day, the month, and the year.
    The program will display the formatted date and the day of the week.
    """
    day = int(input("Key in the day of the month: "))
    month = int(input("Key in the month number (1 = Jan, 2 = Feb, ...): "))
    year = int(input("Key in the year: "))

    y_prime = year - (14 - month) // 12
    leap = y_prime + y_prime // 4 - y_prime // 100 + y_prime // 400
    m_prime = month + 12 * ((14 - month) // 12) - 2
    d_prime = (day + leap + (31 * m_prime) // 12) % 7
    
    # My code here
    d = dt.datetime(year, month, day)
    print(f"{d:%d} {d:%B} {year} is a {d:%A}")

if __name__ == "__main__":
    main()