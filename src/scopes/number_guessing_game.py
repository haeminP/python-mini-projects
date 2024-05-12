import random
from art import logo

# Make function to set difficulty
def set_difficulty():
    mode = input("Choose a difficulty. Type 'easy' or 'hard': ")
    # easy mode gets 10 attempts, hard mode gets 5 attempts
    if mode == "easy":
        return 10
    if mode == "hard":
        return 5

# Function to check user's guess against actual answer
def check_answer(answer, attempts):
    game_over = False
    guess = 0
    while not game_over:
        guess = int(input("Make a guess: "))
        attempts -= 1

        if attempts == 0:
            print("You've run out of guesses, you lose.😔")
            game_over = True
        elif answer > guess:
            print("Too low. Guess again.")
            print(f"You have {attempts} remaining to guess the number.")
        elif answer < guess:
            print("Too high. Guess again")
            print(f"You have {attempts} remaining to guess the number.")
        elif answer == guess:
            print("Hooray! You guessed it right! 🎉")
            game_over = True



def game():
    # Choosing a random number between 1 and 100
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    answer = random.randint(1, 100)
    print(f"Psst, the correct answer is {answer}")
    attempts = set_difficulty()
    print(f"You have {attempts} to try")
    check_answer(answer, attempts)



game()