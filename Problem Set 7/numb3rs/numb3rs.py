"""In a file called numb3rs.py, implement a function called validate that expects an IPv4 address as input as a str 
and then returns True or False, respectively, if that input is a valid IPv4 address or not."""

import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    matches = re.search(r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$", ip)
    if matches:
        a, b, c, d = matches.groups()
        return int(a) < 256 and int(b) < 256 and int(c) < 256 and int(d) < 256
    else:
        return False

if __name__ == "__main__":
    main()