from tkinter import *
import math
import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(timer)
    label.config(text="Timer", bg=YELLOW, fg=RED, font=(FONT_NAME, 50, "normal"))
    canvas.itemconfig(timer_text, text="00:00")
    label_checkmark.config(text="", bg=YELLOW, fg=GREEN)
    global REPS
    REPS = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global REPS
    REPS += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if REPS % 8 == 0:
        countdown(long_break_sec)
        label.config(text="Break", bg=YELLOW, fg=RED, font=(FONT_NAME, 50, "normal"))
    elif REPS % 2 == 0:
        countdown(short_break_sec)
        label.config(text="Break", bg=YELLOW, fg=PINK, font=(FONT_NAME, 50, "normal"))
    else:
        countdown(work_sec)
        label.config(text="Work", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50, "normal"))


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    count_minut = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_minut}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        mark = ""
        for i in range(math.floor(REPS / 2)):
            mark += "✔"
        label_checkmark.config(text=mark, fg=GREEN, bg=YELLOW)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50, "normal"))
label.grid(column=1, row=0)

photo = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=photo)

timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

button_start = Button(text="Start", highlightthickness=0, command=start_timer)
button_start.grid(column=0, row=2)

button_reset = Button(text="Reset", highlightthickness=0, bg=YELLOW, command=reset)
button_reset.grid(column=2, row=2)

label_checkmark = Label(fg=GREEN, bg=YELLOW)
label_checkmark.grid(column=1, row=3)

window.mainloop()
