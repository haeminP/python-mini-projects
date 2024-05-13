import random
from higher_lower_data import data
import higher_lower_art



def print_data(data1, data2):
    print("A: " + data1["name"] + ", a " + data1["description"] + ", from " + data1["country"])
    print(higher_lower_art.vs)
    print("B: " + data2["name"] + ", a " + data2["description"] + ", from " + data2["country"])

def compare_followers(data1, data2):
    a = data1["follower_count"]
    b = data2["follower_count"]

    user_choice = input("Who has more followers? Type 'A' or 'B': ")

    if user_choice == "A" and a > b:
        return data1

    elif user_choice == "B" and b > a:
        return data2

    else:
        return None


def game():
    print(higher_lower_art.logo)
    # randomly choose 2 data from the given list of dictionaries
    data1 = random.choice(data)
    data.remove(data1)
    data2 = random.choice(data)
    data.remove(data2)
    current_score = 0

    print_data(data1, data2)

    new_data = compare_followers(data1, data2)

    while new_data != None:
        current_score += 1
        print(f"You're right! Current score: {current_score}")
        print()
        data1 = new_data
        data2 = random.choice(data)
        data.remove(data2)
        print_data(data1, data2)
        new_data = compare_followers(data1, data2)

    print(f"Sorry you lose. Current score: {current_score}")



game()