"""In a file called faces.py, implement a function called convert that accepts a str as input and returns that same 
input with any :) converted to 🙂 and any :( converted to 🙁. All other text should be returned unchanged. Then, 
in that same file, implement a function called main that prompts the user for input, calls convert on that input, 
and prints the result."""

def convert(str):
    str = str.replace(":)", "🙂")
    str = str.replace(":(", "🙁")
    return str

def main():
    str = input("Write somethong: ")
    result = convert(str)
    print(result)

main()