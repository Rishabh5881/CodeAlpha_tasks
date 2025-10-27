import random

# List of predefined words
words = ["apple", "python", "india", "river", "cloud"]

# Choose a random word
word = random.choice(words)
guessed_letters = []
attempts = 6

print("Welcome to Hangman Game!")
print("_ " * len(word))  # show blanks

while attempts > 0:
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Good guess!")
    else:
        attempts -= 1
        print(f"Wrong guess! Attempts left: {attempts}")

    # Show current progress
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    print(display)

    # Check if player won
    if "_" not in display:
        print("Congratulations! You guessed the word 🎉")
        break
else:
    print(f"Game over! The word was '{word}'.")
