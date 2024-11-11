#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
import random
from replit import clear

MIN_NUMBER = 1
MAX_NUMBER = 100
EASY_LIVES = 10
HARD_LIVES = 5

def difficulty():
	user_input = input("First, please choose a difficulty. Type 'easy' or 'hard': ").lower()
	if user_input == 'easy':
		print("")
		return EASY_LIVES
	elif user_input == 'hard':
		print("")
	else:
		print("Unknown difficulty! Defaulting to Hard.\n")
	return HARD_LIVES
		
def check_guess(nr,answer):
	guess = int(nr)
	if guess == answer:
		return True

	elif guess > answer:
		print("Too high.")
		return False

	elif guess < answer:
		print("Too low.")
		return False

def guessing(answer):
	player_guess = input("Your guess: ")
	if player_guess.isdigit():
		if check_guess(player_guess, answer):
			return True
		else:
			return False
	else:
		print('Invalid guess, you lose a life. Please enter a whole number.')

def game():
	clear()
	print(logo)

	answer = random.randint(MIN_NUMBER,MAX_NUMBER)
	
	print("Welcome to the Guess The Number game!")
	print("Rules are simple: try to guess the number I'm thinking of. \nI will tell you if the number is too high or too low or correct. Good luck!\n")
	
	print(f"The number I'm thinking of is between {MIN_NUMBER} and {MAX_NUMBER}.")
	nr_lives = difficulty()
	
	correct_guess = False
	while nr_lives > 0 and not correct_guess:
		print(f"You have {nr_lives} attempts left to guess the correct number.")
		if guessing(answer):
			print("")
			print(f"You guessed it :D!  The answer was {answer}\n")
			correct_guess = True
		else:
			nr_lives-=1
			if nr_lives != 0:
				print("Guess again.\n")
				
	if nr_lives == 0:
		print(f"You've run out of guesses, you lose :(. I was thinking of {answer}\n")

play= True
while play:
	if input("Would you like to play the Guess The Number game? Type 'y' or 'n': ").lower() == 'y':
		game()
	else:
		play = False
