from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
#---------------------------------LANGUAGE-------------------------------#
language = "French"



#---------------------------------WINDOW-------------------------------#
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
#---------------------------------FLASHCARD IMAGE-------------------------------#
front_card = Canvas(width=800, height=526, bg=BACKGROUND_COLOR)
front_img = PhotoImage(file="./images/card_front.png")
front_card.create_image(400, 263, image=front_img)
front_card.grid(column=1, row=1, columnspan=2)
#---------------------------------BUTTONS-------------------------------#
wrong_img = PhotoImage(file="./images/wrong.png")
x_button = Button(image=wrong_img)
x_button.grid(column=1, row=2)

right_img = PhotoImage(file="./images/right.png")
v_button = Button(image=right_img)
v_button.grid(column=2, row=2)
#---------------------------------WORDS-------------------------------#
language_label = Text(name=language)





#---------------------------------END OF CODE-------------------------------#
window.mainloop()
