"""In a file called um.py, implement a function called count that expects a line of text as input as a str and 
returns, as an int, the number of times that “um” appears in that text, case-insensitively, as a word unto itself, 
not as a substring of some other word."""

import re

def main():
    print(count(input("Text: ")))

def count(s):
    c = re.findall(r"\bum\b", s, re.IGNORECASE)
    return len(c)

if __name__ == "__main__":
    main()