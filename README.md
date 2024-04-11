# Project Title: Hangman Game

## Description
This Python script brings the classic Hangman word guessing game to your terminal! Test your vocabulary and powers of deduction as you try to guess a hidden word letter by letter. Avoid revealing the hangman by making clever guesses before your lives run out.

## Features
- Interactive gameplay with clear user prompts.
- Integrates impressive ASCII art depicting the hangman and the progress of the game.
- Randomly chooses words from a built-in list for a varied playing experience.
- Validates user input to ensure single letters and prevent invalid characters.
- Tracks remaining lives and displays hangman stages for suspense.
- Announces victory when you guess the word correctly or defeat when your lives are depleted.

## How to Play

**1- Run the Script:** Execute the script using python hangman_game.py in your terminal.

**2- Start Guessing:** Type a single letter to guess if it's part of the hidden word.

**3- See the Results:** The script will update the displayed word with the correct guesses and adjust your remaining lives for incorrect ones.

**4- Keep Guessing or Lose (Optional):** Continue guessing letters until you correctly identify all letters in the word (victory) or run out of lives (defeat).

## Example Gameplay

Word: _ _ _ _ _ (5 letters)

Guess a letter: h

You guessed correctly!

Word: h _ _ _ _ (4 letters)

Guess a letter: z

Sorry, 'z' is not in the word. You lose a life!

Word: h _ _ _ _ (4 letters)

Guess a letter: e

You guessed correctly!

Word: he _ _ _ (3 letters)

... (continue guessing letters)

Congratulations! You win. 

The word was 'hello'.

## Contributing
Feel free to contribute to this project by:

- Expanding the word list with various categories (e.g., movies, countries).
- Implementing difficulty levels with varying word lengths or allowed wrong guesses.
- Adding visual themes or sound effects for a more engaging experience.
- To contribute, fork the repository on GitHub and create a pull request with your proposed changes.

## Dependencies
This script relies on two separate Python files:

**- hangman_words.py:** Contains the list of words used in the game.

**- hangman_art.py:** Includes the ASCII art elements for the hangman and stages.

Make sure these files are present in the same directory as **hangman_game.py** for the script to function correctly.
