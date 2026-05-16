import random

# Generate random number
secret_number = random.randint(1, 100)

attempts = 0

print("===== Number Guessing Game =====")
print("Guess a number between 1 and 100")

while True:
    try:
        # User input
        guess = int(input("Enter your guess: "))
        attempts += 1

        # Hint system
        if guess > secret_number:
            print("Too high!")

        elif guess < secret_number:
            print("Too low!")

        else:
            print("Congratulations! You guessed the correct number.")
            print("Total attempts:", attempts)
            break

    # Handle invalid input
    except ValueError:
        print("Please enter a valid number.")