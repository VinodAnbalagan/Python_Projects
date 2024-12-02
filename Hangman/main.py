import random
from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

from hangman_art import logo
print (logo)

# Testing Code
# print(f"Pssst, the word is {chosen_word}.")

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed '{guess}'. Try again!")

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # Check if the user is wrong
    if guess not in chosen_word:
        print(f"{guess} is not in the word. You lose a life!")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lost the game! The word was", chosen_word)

    # Join all the parts of the display into a single string
    print(" ".join(display))

    # Check if user has all the letters
    if "_" not in display:
        end_of_game = True
        print("Congratulations! You've won the game!")
    from hangman_art import stages
    print(stages[lives])




