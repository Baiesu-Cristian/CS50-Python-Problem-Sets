"""In Massachusetts, home to Harvard University, it's possible to request a vanity license plate for your car, with 
your choice of letters and numbers instead of random ones. Among the requirements, though, are:
-All vanity plates must start with at least two letters.
-Vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.
-Numbers cannot be used in the middle of a plate; they must come at the end. The first number used cannot be a '0'.
-No periods, spaces, or punctuation marks are allowed.
In plates.py, implement a program that prompts the user for a vanity plate and then output Valid if meets all of 
the requirements or Invalid if it does not. Assume that any letters in the user's input will be uppercase."""

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def req1(plate):
    return plate[:2].isupper()

def req2(plate):
    length = len(plate)
    return length >= 2 and length <= 6

def req3(plate):
    nr = 0
    for x in plate:
        if x.isdigit():
            if nr == 0 and x == '0':
                return False
            nr = 1
        if x.isupper() and nr == 1:
            return False
    return True

def req4(s):
    return s.isalnum()

def is_valid(s):
    return req1(s) and req2(s) and req3(s) and req4(s)

if __name__ == "__main__":
    main()