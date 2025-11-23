import random
def guess_the_number():
    # 1. Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    # Initialize variables
    guess = 0
    guess_count = 0
    max_guesses = 7 # Optional: Limit the number of tries

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # 2. Keep asking for a guess until the user guesses correctly or runs out of guesses
    while guess != secret_number and guess_count < max_guesses:
        try:
            # Get the user's guess
            guess = int(input(f"Guess #{guess_count + 1} (Max {max_guesses} guesses): Enter your guess: "))
            guess_count += 1
            
            # 3. Give hints
            if guess < secret_number:
                print("Too low! Try a higher number.")
            elif guess > secret_number:
                print("Too high! Try a lower number.")
            
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            
    # Check the final result after the loop ends
    if guess == secret_number:
        print(f"\n🎉 Congratulations! You guessed the number *{secret_number}* correctly in *{guess_count}* guesses!")
    elif guess_count == max_guesses:
        print(f"\nGame Over! You ran out of guesses.")
        print(f"The secret number was *{secret_number}*.")

# Start the game
guess_the_number()