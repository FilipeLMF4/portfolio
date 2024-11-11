from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/french_words.csv")
except pd.errors.EmptyDataError:
    data = pd.read_csv("data/french_words.csv")

data_dict = data.to_dict(orient="records")
current_card = {}


# ------------------------------ END -------------------------------------------- #
def end():
    global flip_timer
    window.after_cancel(flip_timer)
    canvas.delete(card_title)
    canvas.itemconfig(card_word, text="No more words to review!", font=("Ariel", 40, "bold"), fill="black")
    canvas.create_text(400, 350, text="Come back later :)", font=("Ariel", 20, "normal"))
    canvas.itemconfig(card_background, image=front_card)

    flip_button.destroy()
    right_button.destroy()
    wrong_button.destroy()

    exit_button = Button(text="Exit", bd=2, highlightthickness=0, font=("Ariel", 35, "bold"),
                         command=window.destroy, pady=5, padx=50)
    exit_button.grid(column=0, row=1, columnspan=3)


# ------------------------------- NEW CARD --------------------------------------- #
def new_word():
    global current_card, flip_timer, flip_button
    window.after_cancel(flip_timer)

    current_card = random.choice(data_dict)

    flip_button.destroy()
    flip_button = Button(text="FLIP", relief="groove", bd=2, highlightthickness=0, font=("Ariel", 16, "bold"),
                         command=flip_card)
    flip_button.grid(column=1, row=1)

    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], font=("Ariel", 60, "bold"), fill="black")
    canvas.itemconfig(card_background, image=front_card)

    flip_timer = window.after(3000, func=flip_card)


# -------------------------------FLIP CARD--------------------------------------- #
def flip_card():
    global flip_button
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], font=("Ariel", 60, "bold"), fill="white")
    canvas.itemconfig(card_background, image=back_card)

    flip_button.destroy()


# -----------------------------UPDATE DICT------------------------------------- #
def update_dict():
    data_dict.remove(current_card)
    if len(data_dict) == 0:
        end()
    else:
        new_word()


# ------------------------------STARTING UI------------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

front_card = PhotoImage(file="images/card_front.png")
back_card = PhotoImage(file="images/card_back.png")
wrong_image = PhotoImage(file="images/wrong.png")
right_image = PhotoImage(file="images/right.png")

canvas = Canvas(width=810, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_background = canvas.create_image(410, 263, image=front_card)
card_title = canvas.create_text(400, 120, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=3)

right_button = Button(image=right_image, relief="ridge", bd=3, highlightthickness=0, bg=BACKGROUND_COLOR,
                      command=update_dict)
right_button.grid(column=2, row=1)

wrong_button = Button(image=wrong_image, relief="ridge", bd=3, highlightthickness=0, bg=BACKGROUND_COLOR,
                      command=new_word)
wrong_button.grid(column=0, row=1)

flip_button = Button(text="Flip", relief="ridge", bd=2, highlightthickness=0, command=flip_card)
flip_timer = window.after(3000, flip_card)
new_word()

window.mainloop()

pd.DataFrame(data_dict).to_csv("data/words_to_learn.csv", index=False)
