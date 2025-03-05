"""In a file called camel.py, implement a program that prompts the user for the name of a variable in camel case and 
outputs the corresponding name in snake case. Assume that the user’s input will indeed be in camel case."""

str = input("In camel case: ")
res = ""
for char in str:
    if char.isupper():
        res += '_'
        res += char.lower()
    else:
        res += char
print(res)