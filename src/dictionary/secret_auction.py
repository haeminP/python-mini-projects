bid_continue = False
bid_list = {}

while bid_continue:
    name = input("What is your name?")
    bid_price = int(input("How much would you bid?"))
    bid_list[name] = bid_price
    next_round = int("Is there another user who wants to bid?")
    if next_round == "yes":
        bid_continue = True
    elif next_round == "no":
        bid_continue = False

print(bid_list)