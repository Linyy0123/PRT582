"""Lin Yang, s364263"""

import random
"""
Guess the Number Game Module

This module provides functions and a game loop for
playing the Guess the Number game.
The game generates a random 4-digit number,
and the player attempts to guess it while receiving hints.
"""


def generate_random_number():
    """
    Generate a random four-digit number and return it as a string.
    """
    random_number = random.randint(1000, 9999)
    return str(random_number)


def provide_hints(random_number, guessed_number):
    """
    Provide_hints(random_number, guessed_number):
    Generates hints for the guessed number.
    """
    hints = []

    for rand_digit, guessed_digit in zip(
            random_number, guessed_number):
        # Matching digit, add to hints
        if rand_digit == guessed_digit:
            hints.append(rand_digit)
        # Guessed digit is in random number, but not in the same position
        elif guessed_digit in random_number:
            hints.append('0')
        # No match
        else:
            hints.append('-')

    # Combine hints into a single string
    return ''.join(hints)


def play_game():
    """
    Run the Guess the Number Game.

    This function generates a random number,
    allows the player to make guesses,
    provides hints, and ends when the player
    correctly guesses the number or chooses to quit.
    """
    random_number = generate_random_number()
    attempts = 0

    while True:
        guessed_number = input(
            "Enter your guess (4-digit number) or 'q' to quit: ")

        if guessed_number.lower() == 'q':
            print(f"The random number was: {random_number}")
            break

        if not guessed_number.isdigit() or len(guessed_number) != 4:
            print("Invalid input. Please enter a valid 4-digit number.")
            continue

        attempts += 1
        hints = provide_hints(random_number, guessed_number)

        if guessed_number == random_number:
            print(
                f"Great! You guessed the number {random_number} "
                f"in {attempts} attempts.")
            break
        print(f"Hints: {hints}")


def main():
    """
    Start the Guess the Number Game.
    Displays a welcome message and runs the game loop.
    """
    print("Welcome to Guess the Number Game!")

    while True:
        play_game()

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thank you for playing!")
            break


if __name__ == '__main__':
    main()
