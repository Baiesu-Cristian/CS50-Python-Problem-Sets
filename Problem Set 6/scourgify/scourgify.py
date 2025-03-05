"""In a file called scourgify.py, implement a program that:
-Expects the user to provide two command-line arguments:
 -the name of an existing CSV file to read as input, whose columns are assumed to be, in order, name and house, and
 -the name of a new CSV to write as output, whose columns should be, in order, first, last, and house.
-Converts that input to that output, splitting each name into a first name and last name. Assume that each student 
will have both a first name and last name."""

import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif sys.argv[1].endswith(".csv") == False or sys.argv[2].endswith(".csv") == False:
        sys.exit("Not a CSV file")

list = []
try:
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            names = row["name"].split(", ")
            list.append({"first": names[1], "last": names[0], "house": row["house"]})
except FileNotFoundError:
    sys.exit("File does not exist")

with open(sys.argv[2], "w") as file_out:
    writer = csv.DictWriter(file_out, fieldnames=["first", "last", "house"])
    writer.writerow({"first": "first", "last": "last", "house": "house"})
    for row in list:
        writer.writerow({"first": row["first"], "last": row["last"], "house": row["house"]})