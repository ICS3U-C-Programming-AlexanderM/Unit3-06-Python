#!/usr/bin/env python3
# Created By: Alex M
# Date: Oct 19, 2023
# This program makes the user guess a number .
import random


def main():
    # get number from user
    computer_guess = random.randint(1, 9)
    user_guess_as_str = input(" guess a number between 1 - 9 ")
    print("")
    #convert str to an int. if its not an integer 
    try:
        user_guess_as_int = int(user_guess_as_str)
        print("You entered an integer correctly")
        print()

        if user_guess_as_int == computer_guess:
            print(" you got it right ")
        else :
            print("You got it wrong!! ")
            print(f"correct answer is {computer_guess}:")
    except Exception:
         print("This is not an integer")
    finally:
        print(" Thank you for playing :)")


if __name__ == "__main__":
    main()
