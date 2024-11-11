import turtle
import pandas as pd

# Get X and Y values from click on turtle screen
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()


def write_guess(s, x, y):
    state_turtle = turtle.Turtle()
    state_turtle.hideturtle()
    state_turtle.penup()
    state_turtle.goto(x, y)
    state_turtle.write(s, align="center", font=("Arial", 8, "normal"))


def game_over(guesses):
    if guesses == 50:
        prompt = "Congratulations, you guessed all 50 states!"
    else:
        prompt = f"You guessed {guesses}/50 states!"

    game_turtle = turtle.Turtle()
    game_turtle.hideturtle()
    game_turtle.speed("fastest")
    game_turtle.penup()
    game_turtle.goto(0, 250)
    game_turtle.write(prompt, align="center", font=("Arial", 24, "normal"))
    game_turtle.goto(0, -270)
    game_turtle.write("Click on screen to exit", align="center", font=("Arial", 12, "normal"))


screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=800, height=600)

img = "blank_states_img.gif"
screen.addshape(img)

turtle.shape(img)

correct_guesses = []
state_data = pd.read_csv("50_states.csv")

while len(correct_guesses) < 50:
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 States correct",
                                    prompt="Enter a state name.").title()
    if answer_state == "Exit":
        missing_states = []
        for st in state_data.state.to_list():
            if st not in correct_guesses:
                missing_states.append(st)

        df = pd.DataFrame(missing_states)
        df.to_csv("states_to_learn.csv")
        break

    state = state_data[state_data.state == answer_state]
    if len(state) != 0 and answer_state not in correct_guesses:
        correct_guesses.append(answer_state)
        state_x = state.x.iloc[0]
        state_y = state.y.iloc[0]
        write_guess(answer_state, state_x, state_y)

game_over(len(correct_guesses))
screen.exitonclick()
