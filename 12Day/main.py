from art import logo
import random

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")


def decrease_one():
    return number_of_tries - 1


random_number = random.randint(0, 100)

number_of_tries = 5

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == "easy":
    number_of_tries = 10

print(f'You have {number_of_tries} attempts remaining to guess the number.')
number_entered = -1
while number_of_tries > 0:
    number_entered = int(input("Make a guess: "))
    if number_entered > random_number:
        print("Too High")
        print("Try again.")
        number_of_tries = decrease_one()
    elif number_entered < random_number:
        print("Too Low")
        print("Try again.")
        number_of_tries = decrease_one()
    else:
        print(f"You got it! The answer was {random_number}.")
        break
