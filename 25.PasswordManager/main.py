from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- SEARCH WEBSITE ------------------------------- #
def find_password():
    website = website_input.get().title()
    try:
        with open("data.json", mode="r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="No File", message="No Data File Found.")
    except json.decoder.JSONDecodeError:
        messagebox.showerror(title="Empty File", message="No Data Inside File.")
    else:
        if website in data.keys():
            messagebox.showinfo(title=f"{website}",
                                message=f"Email: {data[website]['email']}\nPassword: {data[website]['password']}")
            pyperclip.copy(data[website]['password'])
        else:
            messagebox.showerror(title="No Data", message="No details for website exists.")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    symbols_list = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    numbers_list = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = letters_list + symbols_list + numbers_list

    random.shuffle(password_list)

    password = "".join(password_list)

    password_input.delete(0, END)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get().title()
    user = user_input.get()
    password = password_input.get()
    new_data = {
        website:
            {
                "email": user,
                "password": password,
            },
    }

    if len(website) == 0 or len(user) == 0 or len(password) == 0:
        messagebox.showinfo(title="Valid", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", mode="r") as data:
                details = json.load(data)
                details.update(new_data)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            file = open("data.json", mode="w")
            json.dump(new_data, file, indent=4)
            file.close()
        else:
            with open("data.json", mode="w") as data:
                json.dump(details, data, indent=4)

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

website_input = Entry(width=32)
website_input.grid(column=1, row=1)
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

search_button = Button(text="Search", width=12, command=find_password)
search_button.grid(column=2, row=1)

window.mainloop()
