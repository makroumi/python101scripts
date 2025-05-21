import random  # Import the random module to generate a random number

def number_guessing_game():
    """This function runs a number guessing game where the user has to guess a random number."""
    
    print("🎯 Welcome to the Number Guessing Game!")  # Display welcome message
    print("I have selected a number between 1 and 100. Try to guess it!\n")
    
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    attempts = 0  # Initialize the number of attempts
    guessed_correctly = False  # Boolean flag to track if the user guessed correctly
    
    while not guessed_correctly:  # Keep looping until the user guesses correctly
        try:
            # Get the user's guess and convert it to an integer
            guess = int(input("Enter your guess: "))
            
            # Increase the attempt counter
            attempts += 1
            
            # Check if the guess is correct
            if guess == secret_number:
                print(f"🎉 Congratulations! You guessed the correct number in {attempts} attempts.")
                guessed_correctly = True  # Exit the loop
            elif guess < secret_number:
                print("📈 Too low! Try again.")  # Hint for the user
            else:
                print("📉 Too high! Try again.")  # Hint for the user
        
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")  # Handle non-numeric input

# Run the game
number_guessing_game()
