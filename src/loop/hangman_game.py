import random
from hangman_words import word_list


chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6


from hangman_art import logo
print(logo)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

# create blanks for each letter in the chosen word
display = []
for _ in range(word_length):
    display.append("_")
print(display)

# ask user to guess a letter
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #If the user has entered a ltter they've already guess, let them know
    if guess in display:
        print(f"You've already guessed {guess}")

    #Check the guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Check if user is wrong
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose!")

    #Join all the elements in the list and turn it into a String
    print(f"{' '.join(display)}")

    #Check if user has got all letters
    if "_" not in display:
        end_of_game = True
        print("You win!")

    from hangman_art import stages
    print(stages[lives])
