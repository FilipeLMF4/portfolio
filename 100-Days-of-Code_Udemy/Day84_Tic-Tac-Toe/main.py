from logo import *
import os
import random


def starting_field():
    return r'''
     |     |
  1  |  2  |  3
_____|_____|_____
     |     |
  4  |  5  |  6
_____|_____|_____
     |     |
  7  |  8  |  9
     |     |
'''


def check_victory(choices):
    if 5 in choices:
        if 2 in choices and 8 in choices:
            return True
        elif 4 in choices and 6 in choices:
            return True
        elif 1 in choices and 9 in choices:
            return True
        elif 3 in choices and 7 in choices:
            return True

    if 1 in choices:
        if 4 in choices and 7 in choices:
            return True
        elif 2 in choices and 3 in choices:
            return True

    if 9 in choices:
        if 3 in choices and 6 in choices:
            return True
        if 7 in choices and 8 in choices:
            return True

    return False


def valid_input(choice, field):
    try:
        int_choice = int(choice)
    except ValueError:
        print("Unkown position. Please choose a number from the grid.\n")
        return False
    else:
        if int_choice > 9 or int_choice < 1:
            print("Unknown position. Please choose one from the grid.\n")
            return False
        elif choice not in field:
            print("Position already occupied. Please choose another.\n")
            return False
        else:
            return True


def update_field(curr_field, choice, player):
    if player == 1:
        mark = "X"
    else:
        mark = "O"

    new_field = curr_field.replace(choice, mark)
    return new_field


def start():
    field = starting_field()
    available_positions = list(range(1, 10))
    players = {1: [], 2: []}
    game_on = True
    print(field)
    while game_on:
        for i in range(1, 3):
            if i == 1:
                player_choice = input("Choose a grid position to fill: ")
                while not valid_input(player_choice, field):
                    player_choice = input("Choose a grid position to fill: ")

                os.system("cls")
                print(f"Player's choice: position {player_choice}")
            else:
                player_choice = str(random.choice(available_positions))
                print(f"Opponent's choice: position {player_choice}")

            players[i].append(int(player_choice))
            available_positions.remove(int(player_choice))

            field = update_field(field, player_choice, i)
            print(field)

            if check_victory(players[i]):
                if i == 1:
                    print("YOU WIN!\n")
                else:
                    print("YOU LOSE!\n")
                game_on = False
                break

            if len(available_positions) == 0:
                print("DRAW!\n")
                game_on = False
                break


print(logo)
while input("Would you like to play a game of Tic-Tac-Toe? (Y/N): ").upper() == "Y":
    os.system("cls")
    print("You play first.")
    start()
