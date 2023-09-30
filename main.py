from tkinter import *
import random
import pandas


BACKGROUND_COLOR = "#B1DDC6"
to_learn = {}
current_card = {}
# ---------------------------------READ CSV-------------------------------#
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


# ---------------------------------NEXT CARD-------------------------------#


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=card_front_image)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_image, image=card_back_image)


def is_known():
    to_learn.remove(current_card)
    pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# ---------------------------------WINDOW-------------------------------#


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)
# ---------------------------------FLASHCARD IMAGE-------------------------------#
# FRONT
canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front_image)
canvas.itemconfig(canvas_image, image=card_front_image)
canvas.config(background=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)
# ---------------------------------LETTERS-------------------------------#
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
# ---------------------------------BUTTONS-------------------------------#
wrong_img = PhotoImage(file="images/wrong.png")
x_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
x_button.grid(column=0, row=1)

right_img = PhotoImage(file="images/right.png")
v_button = Button(image=right_img, highlightthickness=0, command=is_known)
v_button.grid(column=1, row=1)
next_card()
# ---------------------------------READ-------------------------------#


# ---------------------------------END OF CODE-------------------------------#
window.mainloop()
