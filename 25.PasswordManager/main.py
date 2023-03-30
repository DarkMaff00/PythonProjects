from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters_list = [random.choice(letters) for letter in range(random.randint(8, 10))]
    symbols_list = [random.choice(symbols) for symbol in range(random.randint(2, 4))]
    numbers_list = [random.choice(numbers) for number in range(random.randint(2, 4))]

    password_list = letters_list + symbols_list + numbers_list

    random.shuffle(password_list)

    password = "".join(password_list)

    password_input.delete(0, END)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    user = user_input.get()
    password = password_input.get()

    if len(website) == 0 or len(user) == 0 or len(password) == 0:
        messagebox.showinfo(title="Valid", message="Please don't leave any fields empty!")
    else:

        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered: \nEmail:{user} \nPassword:{password} "
                                               f"\nIs it ok to save?")

        if is_ok:
            with open("data.txt", mode="a") as data:
                data.write(f"{website} | {user} | {password}\n")
            website_input.delete(0, END)
            password_input.delete(0, END)
            website_input.focus()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

Label(text="Website:").grid(column=0, row=1, pady=10)
Label(text="Email/Username:").grid(column=0, row=2, pady=10)
Label(text="Password:").grid(column=0, row=3, pady=10)

website_input = Entry(width=51)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

user_input = Entry(width=51)
user_input.grid(column=1, row=2, columnspan=2)
user_input.insert(0, "konrad.woj77@gmail.com")

password_input = Entry(width=32)
password_input.grid(column=1, row=3)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=30, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
