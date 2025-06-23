import random
import string

# File from which to load words
WORDLIST_FILENAME = "words.txt"

# Load words from the file
def load_words():
    """Loads a list of words from a file."""
    print("Loading word list from file...")
    with open(WORDLIST_FILENAME, 'r') as inFile:
        line = inFile.readline()
        wordlist = line.split()
    print(f"{len(wordlist)} words loaded.")
    return wordlist

# Randomly select a word from wordlist
def choose_word(wordlist):
    return random.choice(wordlist)

# Check if all letters in secret_word have been guessed
def has_player_won(secret_word, letters_guessed):
    return all(letter in letters_guessed for letter in secret_word)

# Return current word progress: letters guessed or * for unguessed
def get_word_progress(secret_word, letters_guessed):
    return ''.join(letter if letter in letters_guessed else '*' for letter in secret_word)

# Return letters that are still available to guess
def get_available_letters(letters_guessed):
    return ''.join(letter for letter in string.ascii_lowercase if letter not in letters_guessed)

# Reveal a random unguessed letter from the secret word
def reveal_letter(secret_word, letters_guessed):
    hidden = [letter for letter in set(secret_word) if letter not in letters_guessed]
    return random.choice(hidden) if hidden else None

# Main game function
def hangman(secret_word, with_help):
    guesses_remaining = 10
    letters_guessed = []

    print("Welcome to Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")

    while guesses_remaining > 0:
        print("--------------")
        print(f"You have {guesses_remaining} guesses left.")
        print("Available letters:", get_available_letters(letters_guessed))

        guess = input("Please guess a letter: ").lower()

        # Invalid input
        if not guess.isalpha() and guess != "!" or len(guess) != 1:
            print("Oops! That is not a valid letter. Please input a letter from the alphabet:", get_word_progress(secret_word, letters_guessed))
            continue

        # Help option
        if guess == "!":
            if not with_help:
                print("Help is not enabled for this game.")
                continue
            if guesses_remaining < 3:
                print("Sorry, not enough guesses left to use help.")
                continue
            revealed = reveal_letter(secret_word, letters_guessed)
            if revealed:
                print(f"Letter revealed: {revealed}")
                letters_guessed.append(revealed)
                guesses_remaining -= 3
            else:
                print("No unguessed letters to reveal.")
            continue

        # Already guessed letter
        if guess in letters_guessed:
            print("Oops! You've already guessed that letter:", get_word_progress(secret_word, letters_guessed))
            continue

        letters_guessed.append(guess)

        # Correct guess
        if guess in secret_word:
            print("Good guess:", get_word_progress(secret_word, letters_guessed))
        else:
            # Wrong vowel costs 2 guesses, consonant costs 1
            if guess in "aeiou":
                guesses_remaining -= 2
            else:
                guesses_remaining -= 1
            print("Oops! That letter is not in my word:", get_word_progress(secret_word, letters_guessed))

        # Check win condition
        if has_player_won(secret_word, letters_guessed):
            print("--------------")
            print("Congratulations, you won!")
            unique_letters = len(set(secret_word))
            score = (guesses_remaining + 4 * unique_letters) + (3 * len(secret_word))
            print(f"Your total score for this game is: {score}")
            return

    # Game lost
    print("--------------")
    print(f"Sorry, you ran out of guesses. The word was {secret_word}.")

# Start the game
if __name__ == "__main__":
    wordlist = load_words()
    secret_word = choose_word(wordlist)
    with_help = True  # Change to False if no hint support
    hangman(secret_word, with_help)
