from tkinter import *
import pandas as pd
import random

try:
    data = pd.read_csv("data/words_to_learn.csv.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    learn_data = original_data
else:
    learn_data = data.to_dict(orient="records")
    card = {}
# print(data)


def random_word():
    global card, timer
    window.after_cancel(timer)
    card = random.choice(learn_data)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=card["French"], fill="black")
    canvas.itemconfig(card_bg, image=photo_f)
    timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=card["English"], fill="white")
    canvas.itemconfig(card_bg, image=photo_b)


def is_known():
    learn_data.remove(card)
    data = pd.DataFrame(learn_data)
    data.to_csv("data/words_to_learn.csv", index=False)
    random_word()

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
photo_f = PhotoImage(file="images/card_front.png")
photo_b = PhotoImage(file="images/card_back.png")
card_bg = canvas.create_image(400, 263, image=photo_f)
card_title = canvas.create_text(400, 150, text="", fill="black", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", fill="black", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

no_img = PhotoImage(file="images/wrong.png")
yes_img = PhotoImage(file="images/right.png")

button_no = Button(image=no_img, highlightthickness=0, command=random_word)
button_no.grid(column=0, row=1)

button_yes = Button(image=yes_img, highlightthickness=0, command=is_known)
button_yes.grid(column=1, row=1)

random_word()

window.mainloop()
