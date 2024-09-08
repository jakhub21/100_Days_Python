import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. states")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

df = pd.read_csv("50_states.csv")
guess_state = []
list_state = df.state.to_list()


# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()

while len(guess_state) < 50:
    answer_state = screen.textinput(title=f"{len(guess_state)}/{len(list_state)} Guess the state", prompt="Write the state's name").title()
    if answer_state == "Exit":
        missing_states = []
        for state in list_state:
            if state not in guess_state:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("States_To_Learn.csv")
        break
    for states in df["state"]:
        if states == answer_state:
            guess_state.append(states)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = df[df.state == answer_state]
            t.goto(state_data.x.item(), state_data.y.item())
            t.write(answer_state)
