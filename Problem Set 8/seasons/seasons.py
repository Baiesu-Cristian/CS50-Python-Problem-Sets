from datetime import date
import sys
import inflect

def main():
    today = date.today()
    b = input("What's your birthday? ")
    birthday = check_date(b)
    diff = today - birthday
    minutes = diff.days * 24 * 60
    print_words(minutes)

def check_date(b):
    try:
        year, month, day = b.split("-")
        return date(int(year), int(month), int(day))
    except:
        sys.exit("Invalid date")

def print_words(minutes):
    p = inflect.engine()
    words = p.number_to_words(minutes)
    print(words.replace(' and','').capitalize(), "minutes")

if __name__ == "__main__":
    main()
