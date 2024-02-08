#!/usr/bin/env python3

number = 10
guess = '0'

   

while guess != 'q':
    
    try:
        print("I'm thinking of a number...")
        guess = input("Enter what number I am thinking of, or enter 'q' to quit: ")
        
        
        ng = int(guess)

    
        if ng == number:
            print("Congratulations! You guessed the right number.")
            guess = 'q'
        
        elif ng > number:
            print("Wrong, Guess is too high. Try again.")
        elif ng < number:
            print("Wrong, Guess is too Low. Try agian.")

        
    except:
        if guess == 'q':
            guess = 'q'
        else:
            "Please enter a number or q"
    
    

    

print(f"The number was {number}.")