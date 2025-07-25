#  Hangman Game – MIT OCW 6.0001

This is a terminal-based Hangman game developed in Python for Problem Set 2 of MIT’s **6.0001: Introduction to Computer Science and Programming in Python**.

##  Features
- Random word selection from a word list
- Case-insensitive letter guessing
- Tracks guessed letters and remaining lives
- Hint system with `!` key for word suggestions
- Game over messages for win/loss states

##  How to Play

1. The computer randomly selects a word.
2. You have a 10 guesses to figure out the word.
3. Type one letter per turn to guess a character in the word. (for a wrong vowel letter guess 2 guesses are reduced else one guess.)
4. If the guessed letter is in the word, it is revealed. If not, you lose a guess. You can also enter ! to get a hint (reveals a possible correct letter).
5. Win by guessing the word before you run out of guesses.

##  How to Run
```bash
python hangman.py
