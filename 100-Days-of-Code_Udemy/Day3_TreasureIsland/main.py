import art

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

choice1 = input("You find yourself by the beach of a deserted island. The sea stretches out as far as the eyes can see. Your hear a roar coming from the jungle behind you, a terrifying roar that certainly belongs to a hungry wild beast. You must run for safety. Do you go *Left* or *Right*?\n")
print("")

if choice1.lower() == "left":

	print("You decide to go left, hoping to find someplace safe. You manage to hide from the vicious beast, by hiding beneath foliage and rocks you find close by. The beast appears from the jungle, a tiger as big as a boulder. It heads opposite to your location, certainly drawn by the smell of something. You are safe. For now.")
	input("(click to continue)\n")

	print(art.ruins)

	print("You head into the jungle, where you find a lake with a small island in the middle. You manage to spot a small construction on the island, something that resembles an old decrepit building. You think there must be where the treasure is!")
	print("")
	choice2 = input("The lake water seems deep and you can't really see what's beneath. You spot some logs on a nearby bank you could use to build a raft, but there aren't many materials around. Do you *Swim* or try to *Build* a raft?\n")
	print("")

	if choice2.lower() == "build" :
		print("You manage to put together a primtive raft with the logs you spotted and some hanging vines. It seems sturdy enough. You put it in the water and jump on.")
		print("")
		print("Surprisingly, the raft holds up. You use a remaining log to row yourself to the island. On your way you spot what seems like human remains and carnivorous fish. You're relieved you didn't swim!")
		input("(click to continue)\n")

		print(art.doors * 3)

		choice3 = input("You manage to get to the island and get inside the old building. There is nothing inside except for three similar doors painted in different colours, red, blue and green. You believe the treasure is behind one of the doors, but there is no way to know which one. You have to choose. Do you go through the *Red* door, the *Blue* door or the *Yellow* door?\n")
		print("")

		if choice3.lower() == "yellow":
			print("You open the yellow door. It's pitch black and you cannot see anything, but you decide to step through anyway. As soon as you step inside, the door closes behind you. You jump, startled by the sudden slam of the door. When you turn around the room is lit by torches all around with a treasure chest sitting in the middle. You approach and try to open the chest.")
			input("(click to continue)\n")
			print("")

			print (art.coin)
			print("You open the chest to find it full of gold coins. Congratulations, you found the treasure!")

		elif choice3.lower() == "red":
			print("You open the red door. It's pitch black and you cannot see anything, but you decide to step through anyway. As soon as you step inside, the door closes behind you. You jump, startled by the sudden slam of the door. When you turn around the room is engulfed by flames from all sides. You claw at the door, but it won't budge. You cry in despair as fire burns you alive.")
			input("(click to continue)\n")

			print(art.death)
			print("GAME OVER! You died.")

		elif choice3.lower() == "blue":
			print("You open the blue door. It's pitch black and you cannot see anything, but you decide to step through anyway. As soon as you step inside, the door closes behind you. You jump, startled by the sudden slam of the door. When you turn around the room is lit by torches all around with a treasure chest sitting in the middle. You approach and try to open the chest.")
			input("(click to continue)\n")

			print("As soon as you touch the lid, the chest flings open and water starts pouring endlessly from it. The room starts to fill up and there's no way for you to escape. You desperately try to open the door, but it won't budge. You take your last breath of air before the room is completely filled with water.")
			input("(click to continue)\n")

			print(art.death)
			print("GAME OVER! You died.")

        else:
            print("You try to open a door that doesn't exist. The island took a toll on your mental health. GAME OVER!")

	elif choice2.lower() == "swim":
		print("You decide to try swimming to the island. The weather is warm and the island doesn't seem to far away. About halfway there you feel something touching your legs. You try to swim faster, but the touch turns to an excruciating pain, as a piraña gnaws at your leg. You are quickly engulfed by a swarm of the carnivorous fish and cannot swim any further.")
		input("(click to continue)\n")

		print(art.death)
		print("GAME OVER! You died.")
    else:
        print("You could not decide between both actions, so you decide to leave. GAME OVER!")

elif choice1.lower() == 'right':
	print("You decide to go right, hoping to find someplace safe. Unfortunately there seems to be nothing but endless beach and sea. You spot the beast coming out of the jungle, a tiger as big as a boulder. It spots you and stars charging at you at its full speed. You try to escape to sea but the beast catches you before you make it any significant distance. You are quickly shred to pieces by the claws and fangs of the huge feline.")
	input("(click to continue)\n")

	print(art.death)
	print("You died! Try again.")

else:
    print("You could not decide on time and the beast exits the jungle and pounces you immediately. GAME OVER!")
