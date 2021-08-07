# Import random module to randomly choose a word
import random
# Import os for clearing the screen
import os

import hangman_art as art, hangman_words as words

# Print game logo
print(art.logo)

# List of Words
word_list = words.word_list

# Chose a random word from this list
chosen_word = random.choice(word_list)

# For testing display the word on screen
print(f"The chosen word is: {chosen_word}")

# Get length of chosen_word
length = len(chosen_word)

# Create lives variable
lives = 6

# Create a list of '_'
display = ["_" for x in range(length)]

# List to hold letters already guessed
already_guessed = list()

# Run until the word is guessed or lives become 0
while lives > 0:
    # Get user's guess
    guess = input("Please enter a letter: ").lower()

    # if this letter has already been tried/guessed => show message and go to next loop
    if guess in already_guessed:
        print(f"You have already guessed: {guess}")
        continue

    # Append the guess to already_guessed list
    already_guessed.append(guess)

    # Variable to track if guessed letter was found
    guessed_right = False

    # Check against each of the characters of chosen_word
    for i in range(length):
        if chosen_word[i] == guess:
            # Replace '_' with the guessed letter
            display[i] = guess
            guessed_right = True
            #break

    # If guess is incorrect, reduce lives by one
    if guessed_right == False:
        lives -= 1
        print(art.stages[lives])

    # if count of '_' = 0 then break out of loop
    if display.count('_') == 0:
        # All letters have been guessed
        print("Yay! YOU WON!!")
        break

    print(' '.join(display))
    #print(f"Lives Remaining: {lives}")

if lives == 0:
    print("GAME OVER! You Lost.")
