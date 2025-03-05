"""In a file called fuel.py, implement a program that prompts the user for a fraction, formatted as X/Y, wherein 
each of X and Y is an integer, and then outputs, as a percentage rounded to the nearest integer, how much fuel is 
in the tank. If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty. And 
if 99% or more remains, output F instead to indicate that the tank is essentially full. If, though, X or Y is not 
an integer, X is greater than Y, or Y is 0, instead prompt the user again."""

def percentage(prompt):
    while True:
        str = input(prompt)
        try:
            x, y = str.split('/')
            x = int(x)
            y = int(y)
            res = round(x / y * 100)
        except (ValueError, ZeroDivisionError):
            pass
        else:
            if x > y:
                pass
            else:
                return res

def main():
    res = percentage("How much fuel? ")
    if res <= 1:
        print("E")
    elif res >= 99:
        print("F")
    else:
        print(f"{res}%")

if __name__ == "__main__":
    main()