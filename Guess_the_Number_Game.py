import random

def generate_random_number():
    """
    Generate a random four-digit number and return it as a string.
    """
    random_number = random.randint(1000, 9999)
    return str(random_number)

def provide_hints(random_number, guessed_number):
    hints = []

    for i in range(len(random_number)):
        # Matching digit, add to hints
        if random_number[i] == guessed_number[i]:
            hints.append(random_number[i])
        # Guessed digit is in random number, but not in the same position
        elif guessed_number[i] in random_number:
            hints.append('0')
        # No match
        else:
            hints.append('-')

    # Combine hints into a single string
    return ''.join(hints)

def play_game():
    random_number = generate_random_number()
    attempts = 0

    while True:
        guessed_number = input("Enter your guess (4-digit number) or 'q' to quit: ")

        if guessed_number.lower() == 'q':
            print(f"The random number was: {random_number}")
            break

        if not guessed_number.isdigit() or len(guessed_number) != 4:
            print("Invalid input. Please enter a valid 4-digit number.")
            continue

        attempts += 1
        hints = provide_hints(random_number, guessed_number)

        if guessed_number == random_number:
            print(f"Congratulations! You've guessed the number {random_number} in {attempts} attempts.")
            break
        else:
            print(f"Hints: {hints}")


def main():
    print("Welcome to Guess the Number Game!")

    while True:
        play_game()

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thank you for playing!")
            break

if __name__ == '__main__':
    main()
