from art import logo


print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        if highest_bid < bidding_record[bidder]:
            highest_bid = bidding_record[bidder]
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bidding_finished:
    name = input("What is your name? ")
    bid_price = int(input("How much would you bid? $"))
    bids[name] = bid_price
    should_continue = input("Are there any other bidders? Type yes or no\n")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)

