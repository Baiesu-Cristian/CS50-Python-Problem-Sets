"""In a file called coke.py, implement a program that prompts the user to insert a coin, one at a time, each time 
informing the user of the amount due. Once the user has inputted at least 50 cents, output how many cents in change 
the user is owed. Assume that the user will only input integers, and ignore any integer that isn’t an accepted 
denomination."""

current = 0
while current < 50:
    print("Amount Due:", 50 - current)
    coin = int(input("Insert coin: "))
    if coin == 5 or coin == 10 or coin == 25:
        current += coin

print("Change Owed:", current - 50)