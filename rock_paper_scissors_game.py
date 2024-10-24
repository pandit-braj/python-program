import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        return "you win!"
    else:
        return "computer wins!"

def play_game():
    player_score = 0
    computer_score = 0

    while True:
        player_choice = input("Choose rock, paper, or scissors (or 'quit' to end): ").lower()
        
        if player_choice == 'quit':
            print("Thanks for playing!")
            break
        elif player_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid input. Please try again.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        result = determine_winner(player_choice, computer_choice)
        print(result)

        if result == "you win!":
            player_score += 1
        elif result == "computer wins!":
            computer_score += 1

        print(f"Score - You: {player_score}, Computer: {computer_score}")

if __name__ == "__main__":
    play_game()