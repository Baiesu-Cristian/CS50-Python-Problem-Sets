"""In a file called outdated.py, implement a program that prompts the user for a date, anno Domini, in month-day-year 
order, formatted like 9/8/1636 or September 8, 1636. hen output that same date in YYYY-MM-DD format. If the user's 
input is not a valid date in either format, prompt the user again. Assume that every month has no more than 31 days; 
no need to validate whether a month has 28, 29, 30, or 31 days."""

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("Date: ")
    try:
        if "/" in date:
            month, day, year = date.split("/")
        elif "," in date:
            month_day, year = date.split(", ")
            month, day = month_day.split(" ")
            month = (months.index(month)) + 1
        if int(month) > 12 or int(day) > 31:
            raise ValueError
    except (ValueError, NameError):
        pass
    else:
        print(f"{int(year)}-{int(month):02}-{int(day):02}")
        break