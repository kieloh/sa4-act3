#!/usr/bin/env python3

number = '10'
guess = '0'



while guess != 'q':
    

    print("I'm thinking of a number...")
    guess = input("Enter what number I am thinking of, or enter 'q' to quit: ")
    
    if guess == number:
        print("Congratulations! You guessed the right number.")
        guess = 'q'
    elif guess == 'q':
        guess = 'q'
    else:
        print("Wrong, Try again.")

    
    



print(f"The number was {number}.")