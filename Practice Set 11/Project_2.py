import random

random_number = random.randint(1, 100)
print("Random number is generated between 1 to 100. Try to guess it!")

guess = None
guess_count = 0

while guess != random_number:
    guess = int(input("\nEnter your guess: "))
    guess_count += 1

    if guess > random_number:
        print("Lower number please! guess again.")
    
    elif guess < random_number:
        print("\nHigher number please! guess again.")
    else:
        print("\nCongratulations! You guessed the number.")
        print(f"It took you {guess_count} guesses.")
        break