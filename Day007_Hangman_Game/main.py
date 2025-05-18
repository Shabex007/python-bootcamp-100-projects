import random
from word_list import words, states, logo


def choose_word(category):
    """Choose a random word from the specified category."""
    return random.choice(words[category])


def display_word(word, guessed_letters):
    """Display the current state of the word with guessed letters."""
    return ' '.join(letter if letter in guessed_letters else '_' for letter in word)


def get_valid_category():
    """Prompt the user for a valid category until a correct one is entered."""
    while True:
        category = input("Enter category (countries, animals, fruits_veggies, foods): ").strip().lower()
        if category in words:
            return category
        print("Invalid category. Please choose from the available categories.")


def hangman():
    """Main function to run the Hangman game."""
    print(logo)
    print("Welcome to Hangman!")

    category = get_valid_category()
    word_to_guess = choose_word(category)
    guessed_letters = set()
    lives = 7

    while lives > 0:
        print("\n" + display_word(word_to_guess, guessed_letters))
        print(f"Remaining lives: {lives}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print(f"You already guessed the letter '{guess}'. Try again!")
            continue

        guessed_letters.add(guess)

        if guess in word_to_guess:
            print(f"Good job! '{guess}' is in the word.")
        else:
            print(f"'{guess}' is not in the word.")
            lives -= 1

        if all(letter in guessed_letters for letter in word_to_guess):
            print(f"\nCongratulations! You guessed the word '{word_to_guess}'!")
            break

        print(states[lives])

    else:
        print(f"\nGame over! The word was '{word_to_guess}'.")


if __name__ == "__main__":
    hangman()