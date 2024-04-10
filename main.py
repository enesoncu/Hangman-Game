import os
import random
from hangman_words import word_list
from hangman_art import stages, logo

def get_guess(display):
    while True:
        guess = input("Guess a letter: ").lower()
        clear()

        if len(guess) != 1:
            print("Please enter only one letter.")
        elif guess in display:
            print(f"You've already guessed '{guess}'.")
        elif not guess.isalpha():
            print("Please enter a valid letter.")
        else:
            return guess

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)
    end_of_game = False
    lives = 6
    display = ["_" for _ in range(word_length)]

    print(logo)

    while not end_of_game:
        guess = get_guess(display)

        if guess in chosen_word:
            for position in range(word_length):
                if chosen_word[position] == guess:
                    display[position] = guess
        else:
            lives -= 1
            print(f"Sorry, '{guess}' is not in the word. You lose a life!")
            if lives == 0:
                end_of_game = True
                print(f"The word was '{chosen_word}'. You lose.")

        print(f"{' '.join(display)}")
        print(stages[lives])

        if "_" not in display:
            end_of_game = True
            print("Congratulations! You win.")

if __name__ == "__main__":
    main()
