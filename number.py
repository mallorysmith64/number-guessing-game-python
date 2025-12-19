import random

name = input("Enter your name: ")
print("Welcome to number guesser, " + name + "!")
print("I'm thinking of a number between 1 and 100.")
print("Please select a difficulty. Type 'easy' or 'hard':")

difficulty = input().lower()
if difficulty == "easy":
    attempts = 10
else:
    attempts = 5

print("You have " + str(attempts) + " attempts to guess the number.")

guessed_number = random.randint(1, 100)
while attempts > 0:
    print("Make a guess:")
    user_guess = int(input())
    
    if user_guess < guessed_number:
        print("Too low.")
    elif user_guess > guessed_number:
        print("Too high.")
    else:
        print("Congratulations, " + name + "! You've guessed the number " + str(guessed_number) + " correctly!")
        break

    attempts -= 1
    if attempts > 0:
        print("You have " + str(attempts) + " attempts remaining.")
    else:
        print("Sorry, you've run out of attempts. The number was " + str(guessed_number) + ".")