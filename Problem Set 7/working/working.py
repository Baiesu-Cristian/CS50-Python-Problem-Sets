"""In a file called working.py, implement a function called convert that expects a str in any of the 12-hour 
formats below and returns the corresponding str in 24-hour format (i.e., 9:00 to 17:00). Expect that AM and PM will 
be capitalized (with no periods therein) and that there will be a space before each. Assume that these times are 
representative of actual times, not necessarily 9:00 AM and 5:00 PM specifically."""

import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    matches = re.search(r"(\d+):?(\d*) (\w+) to (\d+):?(\d*) (\w+)", s)
    if not matches or (matches.group(2) != "" and int(matches.group(2)) > 59) or (matches.group(5) != "" and int(matches.group(5)) > 59):
        raise ValueError
    h = matches.groups()
    if h[2] == "PM":
        h1 = int(h[0]) + 12
        if h1 == 24:
            h1 = "12"
    else:
        h1 = int(h[0])
        if h1 == 12:
            h1 = "00"
    if h[5] == "PM":
        h2 = int(h[3]) + 12
        if h2 == 24:
            h2 = "12"
    else:
        h2 = int(h[3])
        if h2 == 12:
            h2 = "00"
    if h[1] == "":
        m1 = "00"
    else:
        m1 = h[1]
    if h[4] == "":
        m2 = "00"
    else:
        m2 = h[4]
    return f"{h1:02}:{m1} to {h2:02}:{m2}"

if __name__ == "__main__":
    main()