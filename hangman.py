import random

word = "python"

guessed_letters = []

print("Welcome to Hangman!")

while True:
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print(display_word)

    if "_" not in display_word:
        print("Congratulations! You Won!")
        break

    guess = input("Enter a letter: ")

    guessed_letters.append(guess)