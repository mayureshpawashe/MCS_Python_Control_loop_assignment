#Write a Python program to guess a number between 1 to 9. Note: User is prompted to enter a guess.
# If the user guesses wrong then the prompt appears again until the guess is correct, on successful guess
# , user will get a "Well guessed!" message, and the program will exit.
from random import randint
r=randint(0,9)
while(True):
    n = int(input("Enter any Random Number to Guess::"))
    if r==n:
        print("::::Correct Guess Well Done::::")
        break
    else:
        print("Try Again")
        continue