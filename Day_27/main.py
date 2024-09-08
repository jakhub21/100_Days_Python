import tkinter


def button_clicked():
    new_text = float(input_value.get())
    km = round(new_text * 1.609)
    value.config(text=km)


window = tkinter.Tk()
window.title("Calculator Mile To Km")
window.minsize(width=250, height=100)
window.config(padx=10, pady=10)

input_value = tkinter.Entry(width=7)
input_value.grid(column=1, row=0)

my_label = tkinter.Label(text="Miles", font=("Arial", 18, "normal"))
my_label.grid(column=2, row=0)

my_text = tkinter.Label(text="is equal to", font=("Arial", 18, "normal"))
my_text.grid(column=0, row=1)

value = tkinter.Label(text="0", font=("Arial", 18, "normal"))
value.grid(column=1, row=1)

km_text = tkinter.Label(text="Km", font=("Arial", 18, "normal"))
km_text.grid(column=2, row=1)

button = tkinter.Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

window.mainloop()
