import random
import Guess_logo
easy_level = 10
hard_level = 5

def difficulty_level(level):
    if level == 'easy':
        return easy_level
    elif level == 'hard':
        return hard_level
    else:
        print()

def correctness (Cguess,my_guess,attempts):
    if my_guess < Cguess:
        print("You guessed a lower number.\n")
        return attempts-1
    elif my_guess > Cguess:
        print("You guessed a higher number.\n")
        return attempts-1
    else:
        print(f"\nYour guess is correct and the number is {my_guess}.\n")

def Game():
    print(Guess_logo.logo)
    # print("Let me guess a number between 1 to 50.")
    Cguess = random.randint(1,50)
    # print(Cguess)
    difficulty = input("Choose level of difficulty. Type 'easy' or 'hard': ").lower()

    # Calling Function "difficulty Level"
    attempts = difficulty_level(difficulty)
    if attempts != easy_level and attempts != hard_level:
        print("Incorrect Choice")
        return Game()
    my_guess = 0
    while my_guess!=Cguess:
        print(f"You have {attempts} remaining to guess the correct number.")
        my_guess = int(input("Guess a number : "))
        attempts=correctness (Cguess,my_guess,attempts) # Check answer if guessed number matched or not.
        if attempts == 0:
            print("Your attempts are over....... You lose!\n")
            return
        elif my_guess!=Cguess:
            print("Guess Again!\n")
Game()

