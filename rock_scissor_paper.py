import random

def play_game():
    player_wins = 0
    computer_wins = 0
    
    print("\n--- Rock Paper Scissors ---")
    print("First to 2 wins! (Type r/p/s)")

    while player_wins < 2 and computer_wins < 2:
        # Input with validation
        while True:
            player_choice = input("Choose [r]ock, [p]aper, or [s]cissors: ").lower()
            if player_choice in ['r', 'p', 's']:
                break
            print("Invalid input! Please enter r, p, or s.")

        # Map letters to full words
        choice_map = {'r': 'rock', 'p': 'paper', 's': 'scissors'}
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        
        print(f"You chose: {choice_map[player_choice]}")
        print(f"Computer chose: {computer_choice}")

        # Determine winner
        player_full_choice = choice_map[player_choice]
        if (player_full_choice == "rock" and computer_choice == "scissors") or \
           (player_full_choice == "scissors" and computer_choice == "paper") or \
           (player_full_choice == "paper" and computer_choice == "rock"):
            print("You won this round!")
            player_wins += 1
        elif player_full_choice == computer_choice:
            print("It's a tie!")
        else:
            print("Computer won this round!")
            computer_wins += 1

        print(f"Score -> You: {player_wins} | Computer: {computer_wins}\n")

    # Final result
    if player_wins > computer_wins:
        print("🎉 Congratulations! You won the game!")
    else:
        print("😢 Computer won the game!")

# Main game loop
while True:
    play_game()
    
    # Play again prompt with validation
    while True:
        replay = input("\nPlay again? (y/n): ").lower()
        if replay in ['y', 'n']:
            break
        print("Invalid input! Please enter y or n.")
    
    if replay == 'n':
        print("Thanks for playing!")
        break