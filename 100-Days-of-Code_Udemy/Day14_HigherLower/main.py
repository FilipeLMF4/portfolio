from game_data import data
from art import logo, vs
import random
from replit import clear

def format_data(dat):
	return f"{dat['name']}, a {dat['description']}, from {dat['country']}."
	
def game():
	print(logo)
	
	current_score = 0
	itemA = random.choice(data)
	game_on = True
	
	while game_on == True:
		itemB = random.choice(data)
		while itemB == itemA:
			itemB = random.choice(data)
	
		more_followers = 'A'
		if itemA['follower_count'] < itemB['follower_count']:
			more_followers = 'B'
			
		print(f"A: {format_data(itemA)}")
		print(vs)
		print(f"B: {format_data(itemB)}")
		
		user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()
		
		clear()
		print(logo)
		if user_choice == more_followers:
			current_score += 1
			print(f"Correct! Current score: {current_score}")
			itemA = itemB
		else:
			print("Sorry, that's wrong :(!")
			print(f"Final score: {current_score}")
			game_on = False
			print("")
			

while input("Would you like to play the higher/lower game? Type 'y' or 'n': ").lower() == 'y':
	clear()
	game()
	