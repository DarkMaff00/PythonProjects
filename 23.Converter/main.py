from tkinter import *


def lbs_to_kg():
    lbs = float(prompt.get())
    kg = round(lbs * 0.45359237, 2)
    result.config(text=f"{kg}")


window = Tk()
window.title("Lbs to Kg Converter")
window.config(pady=20, padx=20)

prompt = Entry(width=10)
prompt.insert(0, "0")
prompt.grid(column=1, row=0)

Label(text="Lbs").grid(column=2, row=0)
Label(text="is equal to").grid(column=0, row=1)
result = Label(text="0")
result.grid(column=1, row=1)
Label(text="Kg").grid(column=2, row=1)

button = Button(text="Calculate", width=10, command=lbs_to_kg)
button.grid(column=1, row=2)

window.mainloop()
