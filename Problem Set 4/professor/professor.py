"""In a file called professor.py, implement a program that:
-Prompts the user for a level, n. If the user does not input 1, 2, or 3, the program should prompt again.
-Randomly generates ten math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with 
n digits. No need to support operations other than addition.
-Prompts the user to solve each of those problems. If an answer is not correct (or not even a number), the program 
should output EEE and prompt the user again, allowing the user up to three tries in total for that problem. If the 
user has still not answered correctly after three tries, the program should output the correct answer.
-The program should ultimately output the user's score: the number of correct answers out of 10."""

import random

def main():
    score = 0
    level = get_level()
    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)

        for j in range(3):
            try:
                guess = int(input((f"{x} + {y} = ")))
                if guess == x + y:
                    score += 1
                    break
                else:
                    raise ValueError
            except ValueError:
                print("EEE")
        if guess != x + y:
                print(f"{x} + {y} = {x + y}")
    print(f"Score: {score}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass

def generate_integer(level):
    if level == 1:
        n = random.randint(0, 9)
    elif level == 2:
        n = random.randint(10, 99)
    else:
        n = random.randint(100, 999)
    return n

if __name__ == "__main__":
    main()