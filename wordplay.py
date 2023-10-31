import random

# Predefined words for different levels
words = {
    "Beginners": ["apple", "banana", "cherry", "grape", "lemon","table", "chair", "light", "apple", "house", "water", "tiger", "dance", "happy",    "ocean"],
    "Moderate": ["elephant", "giraffe", "kangaroo", "penguin", "rhinoceros","freedom", "picture", "journey", "breathe", "village", "whisper", "stretch", "musical", "mystery", "weather"],
    "Expert": ["congratulations", "exaggeration", "perpendicular", "unbelievable","comprehensive", "procrastinate", "transformation", "alphabetically", "unbelievable", "intentionally", "independence", "multiplication", "spontaneity", "electricity"]
}

# Function to select a random word based on the level
def select_word(level):
    return random.choice(words.get(level, []))

# Function to validate user input (single alphabet character)
def validate_input(user_input):
    if user_input.isalpha() and len(user_input) == 1:
        return True
    else:
        print("Please enter a single alphabet character.")
        return False

# Function to play the game
def play_game(level, max_attempts):
    # Select a random word for the given level
    secret_word = select_word(level)
    
    # Initialize the guessed word with underscores
    guessed_word = ["_"] * len(secret_word)
    
    attempts = 0

    print("Welcome to the Word Guessing Game!")
    print("Level: " + level)
    print("Word: " + " ".join(guessed_word))

    while attempts < max_attempts:
        user_guess = input("Guess a letter: ").lower()

        # Validate user input
        if validate_input(user_guess):
            if user_guess in secret_word:
                for i in range(len(secret_word)):
                    if secret_word[i] == user_guess:
                        guessed_word[i] = user_guess
                print("Word: " + " ".join(guessed_word))
                if "_" not in guessed_word:
                    print("Congratulations! You guessed the word:", secret_word)
                    break
            else:
                attempts += 1
                remaining_attempts = max_attempts - attempts
                print(f"Incorrect guess. {remaining_attempts} attempts remaining.")
        else:
            continue

    if "_" in guessed_word:
        print("Out of attempts. The word was:", secret_word)

# Main game loop
if __name__ == "__main__":
    while True:
        level = input("Choose a level (Beginners/Moderate/Expert): ").capitalize()
        if level in words:
            play_game(level, max_attempts=6)
            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again != "yes":
                break
        else:
            print("Invalid level. Please choose from Beginners, Moderate, or Expert.")
