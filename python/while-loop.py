print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

import random
number = random.randint(1, 10)  # Generate a random number between 1 and 10
isGuessRight = False  # Initialize a flag to track correct guesses

while isGuessRight != True:  # Run the game until the guess is correct
    guess = input("Guess a number between 1 and 10: ")  # Ask user to guess
    if int(guess) == number:  # Check if the guess matches the generated number
        print("You guessed {}. That is correct! You win!".format(guess))  # Correct guess message
        isGuessRight = True  # Set the flag to end the game
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))  # Incorrect guess message