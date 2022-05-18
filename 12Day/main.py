from art import logo
from random import randint

EASY = 10
HARD = 5
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

random_number = randint(0, 100)


def set_difficulty():
    number_of_tries = HARD
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        number_of_tries = EASY
    return number_of_tries


def game():
    def decrease_one():
        return guess - 1

    guess = set_difficulty()
    print(f'You have {guess} attempts remaining to guess the number.')
    number_entered = -1
    while guess > 0:
        number_entered = int(input("Make a guess: "))
        if number_entered > random_number:
            print("Too High")
            print("Try again.")
            guess = decrease_one()
            print(f'You have {guess} attempts remaining to guess the number.')
        elif number_entered < random_number:
            print("Too Low")
            print("Try again.")
            guess = decrease_one()
            print(f'You have {guess} attempts remaining to guess the number.')
        else:
            print(f"You got it! The answer was {random_number}.")
            break

    if guess == 0:
        print("You've run out of guesses, you lose.")
        print(f'The number was: {random_number}')


game()
