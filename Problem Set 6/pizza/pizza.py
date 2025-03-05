"""In a file called pizza.py, implement a program that expects exactly one command-line argument, the name (or path) 
of a CSV file in Pinocchio's format, and outputs a table formatted as ASCII art using tabulate. Format the table 
using the library's grid format. If the user does not specify exactly one command-line argument, or if the specified 
file's name does not end in .csv, or if the specified file does not exist, the program should instead exit via sys.exit."""

import sys
import csv
from tabulate import tabulate

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif sys.argv[1].split('.')[1] != "csv":
    sys.exit("Not a Python file")

try:
    file = open(sys.argv[1])
except FileNotFoundError:
    sys.exit("File does not exist")

menu = []
reader = csv.reader(file)

for row in reader:
        menu.append(row)

print(tabulate(menu[1:], menu[0], tablefmt="grid"))

file.close()