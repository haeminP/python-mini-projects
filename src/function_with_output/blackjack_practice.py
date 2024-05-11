import random
from art_blackjack import logo

def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards):
    """
    Take a list of cards and return the score calculated from the cards
    0 will represent a blackjack in our game.
    If the score is already over 21, remove the 11 and replace it with a 1"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0 or computer_score > 21:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😊"
    elif user_score > computer_score:
        return "You win 😊"
    else:
        return "You lose 😭"


def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False

    #deal first two cards to the user and dealer
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    #user's turn to play the game
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"    Your cards: {user_cards}, current score: {user_score}")
        print(f"    Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True

        else:
            user_want_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_want_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    #computer's turn to play game
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"    Your final hand: {user_cards}, final score: {user_score}")
    print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()