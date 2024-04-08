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

# create an empty list
# For each letter in the chosen_word, add a "_" to the list
display = []
for _ in range(len(chosen_word)):
    display.append("_")
print(display)

# ask user to guess a letter
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #check guessed letter
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose!")

    print(f"{' '.join(display)}")


    if "_" not in display:
        end_of_game = True
        print("You win!")

    from hangman_art import stages
    print(stages[lives])
