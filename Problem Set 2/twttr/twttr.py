"""In a file called twttr.py, implement a program that prompts the user for a str of text and then outputs that 
same text but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase."""

str = input("Write something: ")
res = ""
for char in str:
    if char not in ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']:
        res += char
print(res)