import random

def welcome():
    print("Welcome to the Number Guessing Game!")
    name = input("What's your name? ")
    print(f"Hello, {name}! I'm thinking of a number between 1 and 100.")
    print("You have 10 attempts to guess the number. Let's begin!")

def play_game():
    secret_number = random.randint(1, 100)
    attempts = 0

    while attempts < 10:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {secret_number} correctly in {attempts} attempts.")
            return

    print(f"Game over! The secret number was {secret_number}.")
    
def main():
    welcome()
    while True:
        play_game()
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thank you for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
