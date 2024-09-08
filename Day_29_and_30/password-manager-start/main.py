from tkinter import *
from tkinter import messagebox
import random
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def random_pass():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password = []
    for l in range(1, nr_letters+1):
        choice = random.choice(letters)
        password.append(choice)

    for s in range(1, nr_symbols+1):
        choice = random.choice(symbols)
        password.append(choice)

    for n in range(1, nr_numbers+1):
        choice = random.choice(numbers)
        password.append(choice)

    generate_pass = ""

    for i in range(1, len(password)+1):
        choice = random.choice(password)
        generate_pass += choice
        password.remove(choice)

    input_pass.insert(0, generate_pass)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_to_file():
    new_data = {
        input_web.get(): {
            "email": input_mail.get(),
            "password": input_pass.get()
    }
    }
    if len(input_web.get()) == 0 or len(input_pass.get()) == 0 or len(input_mail.get()) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any empty field")
    else:
        is_ok = messagebox.askokcancel(title=input_web.get(), message=f"Details: \nEmail: {input_mail.get()}\n"
                                                                      f"Password: {input_pass.get()}\nIs it ok to save?")
        if is_ok:
            try:
                with open("pass.json", "r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("pass.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open("pass.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                input_web.delete(0, END)
                input_pass.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = input_web.get()
    try:
        with open("pass.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="There is no such file")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"{website}\nYour email: {email}\nYour password: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"There are no details for {website} exists")



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
photo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo)
canvas.grid(column=1, row=0)

web_label = Label(text="Website:")
web_label.grid(column=0, row=1)

input_web = Entry(width=21)
input_web.grid(column=1, row=1)
input_web.focus()

button_gen_pass = Button(text="Search", width=7, command=find_password)
button_gen_pass.grid(column=2, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

input_mail = Entry(width=35)
input_mail.grid(column=1, row=2, columnspan=2)
input_mail.insert(0, "jakhub21@gmail.com")

pass_label = Label(text="Password:")
pass_label.grid(column=0, row=3)

input_pass = Entry(width=21)
input_pass.grid(column=1, row=3)

button_gen_pass = Button(text="Generate", width=7, command=random_pass)
button_gen_pass.grid(column=2, row=3)

button_add = Button(text="Add", width=36, highlightthickness=0, command=save_to_file)
button_add.grid(column=1, row=4, columnspan=2)

window.mainloop()
