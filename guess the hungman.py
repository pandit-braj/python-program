import random

def display_hangman(tries):
    stages = [
        """
           -----
           |   |
           |   O
           |  /|\\
           |  / \\
           |
        """,
        """
           -----
           |   |
           |   O
           |  /|\\
           |  /
           |
        """,
        """
           -----
           |   |
           |   O
           |  /|
           |
           |
        """,
        """
           -----
           |   |
           |   O
           |   |
           |
           |
        """,
        """
           -----
           |   |
           |   O
           |
           |
           |
        """,
        """
           -----
           |   |
           |
           |
           |
           |
        """,
        """
           -----
           |
           |
           |
           |
           |
        """,
    ]
    return stages[tries]

def get_word():
    words = ["python", "hangman", "challenge", "programming", "developer"]
    return random.choice(words)

def play_game():
    word = get_word()
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    tries = 6

    print("Welcome to Hangman!")
    print(display_hangman(tries))
    print(f"Word to guess: {word_completion}\n")

    while not guessed and tries > 0:
        guess = input("Please guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
            word_completion = "".join([letter if letter in guessed_letters else "_" for letter in word])
        else:
            tries -= 1
            print(f"Sorry, '{guess}' is not in the word. You have {tries} tries left.")

        print(display_hangman(tries))
        print(f"Word to guess: {word_completion}\n")

        if "_" not in word_completion:
            guessed = True

    if guessed:
        print(f"Congratulations! You've guessed the word: '{word}'")
    else:
        print(f"Sorry, you've run out of tries. The word was: '{word}'")

def main():
    while True:
        play_game()
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
