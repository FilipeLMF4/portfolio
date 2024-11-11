import time
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

print("Welcome to the Rock, Paper, Scissors International Worldcup Extravaganza Tournament final. It all comes down to this.")
time.sleep(1)
print("To challenge the fifteen times World Champion of Rock, Paper, Scissors, comes a new player on the RPS scene. Will they have what it takes to defeat the king, or will they leave with the bitter taste of defeat in their mouth? Only one way to find out!")
time.sleep(3)
print("")
player_choice = input("Player, choose your weapon!\n0 - Rock\n1 - Paper\n2 - Scissors\n(Type the digit corresponding to your choice)\n")
print("")

if not player_choice.isdigit():
	print("That is not a valid choice for Rock, Paper, Scissors! Disqualified!")
elif (int(player_choice) >=3) or (int(player_choice)<0):
	print("That is not a valid choice for Rock, Paper, Scissors! Disqualified!")
else:
	player_choice = int(player_choice)
	compare_list=[0,1,2]
	hands = [rock,paper,scissors]
	opponent_choice = random.randint(0,2)
	
	print("All right, the moment we've all been waiting for!")
	time.sleep(2)
	print("It's ROCK")
	time.sleep(0.5)
	print("PAPER")
	time.sleep(0.5)
	print("SCISSORS")
	time.sleep(0.5)
	print("SHOOT")
	time.sleep(0.5)
	
	print("")
	print(f"Player hand:\n{hands[player_choice]}")
	print(f"Opponent hand:\n{hands[opponent_choice]}")
	
	if player_choice == opponent_choice:
		print("It's a Draw!")
	elif compare_list[player_choice-1] == compare_list[opponent_choice]:
		print("You Win!")
		time.sleep(1)
		print("Congratulations, you're the new World Champion of Rock, Paper, Scissors!")
	else:
		print("You lose!")
		time.sleep(1)
		print("It was not this time that the champion was dethroned! Better luck next time.")