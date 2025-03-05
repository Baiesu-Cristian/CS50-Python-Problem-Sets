"""In meal.py, implement a program that prompts the user for a time and outputs whether it’s breakfast time, lunch 
time, or dinner time. If it’s not time for a meal, don’t output anything at all. Assume that the user’s input will 
be formatted in 24-hour time as #:## or ##:##. And assume that each meal’s time range is inclusive. For instance, 
whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime in between, it’s time for breakfast."""

def main():
    str = input("What's the time? ")
    time = convert(str)
    if time >= 7 and time <= 8:
        print("breakfast time")
    elif time >= 12 and time <= 13:
        print("lunch time")
    elif time >= 18 and time <= 19:
        print("dinner time")

def convert(time):
    x, y = time.split(':')
    return float(x) + (float(y) * 100 / 6000)

if __name__ == "__main__":
    main()