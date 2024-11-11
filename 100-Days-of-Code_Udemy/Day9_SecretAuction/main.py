from replit import clear
import art
#HINT: You can call clear() to clear the output in the console.

print(art.logo)
print("Welcome to the secret auction.")
auction = True
bids_dictionary = {}
highest_bid = 0
while auction:
	name = input("Please enter your name: ")
	bid = int(input("Please enter your bid: $"))

	bids_dictionary[name] = bid
	if bid > highest_bid:
		winner = name
		highest_bid = bid

	other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
	
	if other_bidders == "no":
		auction = False

	clear()

print(f"The winner is {winner} with a bid of ${bids_dictionary[winner]}")

