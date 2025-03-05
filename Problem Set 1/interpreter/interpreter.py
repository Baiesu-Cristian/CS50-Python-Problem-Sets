"""In a file called interpreter.py, implement a program that prompts the user for an arithmetic expression and then 
calculates and outputs the result as a floating-point value formatted to one decimal place."""

str = input("Write an expression: ")
x, y, z = str.split()
match y:
    case "+":
        print(float(x) + float(z))
    case "-":
        print(float(x) - float(z))
    case "*":
        print(float(x) * float(z))
    case "/":
        print(float(x) / float(z))