from flask import Flask
import random

app = Flask(__name__)
solution = random.randint(0, 9)
print(f"Psst. Solution is {solution}")


@app.route('/')
def main_page():
    return ("<h1>Guess a number between 0 and 9</h1>"
            "<img src=https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif>")


@app.route('/<guess>')
def user_guess(guess):
    try:
        iguess = int(guess)
    except ValueError:
        return (f"<h1 style='color: red'>Invalid input, '{guess}' is not a number! Please input a whole number.</h1>"
                f"<img src=https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcmJ2cW13cWE3dmdkc3Q4dGdxdjV0Ynp1NnJ2MXl5dTM0M2RhZzh3aSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/JT7Td5xRqkvHQvTdEu/giphy.gif width=600>")
    else:
        additional_text=""
        if int(guess) > 9:
            additional_text = "<em><b><p style='color: black'>Also, number is between 0 and 9.</p></b></em>"
        if int(guess) > solution:
            return ("<h1 style='color: orange'>Too high, try again!</h1>"
                    "<img src=https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif>"
                    f"{additional_text}")
        elif int(guess) < solution:
            return ("<h1 style='color: blue'>Too low, try again!</h1>"
                    "<img src=https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif>")
        else:
            return ("<h1 style='color: green'>You found me!</h1>"
                    "<img src=https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif>")


if __name__ == "__main__":
    # Run the app in debug mode to auto-reload
    app.run(debug=True)
