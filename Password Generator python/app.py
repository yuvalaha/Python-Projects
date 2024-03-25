
from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------------------------Constants---------------------------------------------

BG = '#FFF8E8'
LABEL_FG = '#7B3F00'
LABEL_FONT = ("ariel", 16, "bold")
ENTRY_FONT = ("ariel", 13, "bold")


small_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
big_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
               'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# ---------------------------------------Main window and Canvas--------------------------------------

# Creating the main window
window = Tk()
window.config(padx=60, pady=60, background=BG)
window.title(string="Password Generator")

# Creating the canvas
canvas = Canvas(width=500, height=500, highlightthickness=0, background=BG)
# Creating the password image
password_image = PhotoImage(file="password.png")
canvas.create_image(150, 200, image=password_image)
canvas.grid(row=0, column=1)

# ----------------------------------Creating txt file with all data---------------------------------


def save_data_txt():

    website_txt = website_entry.get()
    email_txt = email_entry.get()
    password_txt = password_entry.get()

    # Check if the user forgot to enter data in the texts box
    if len(website_txt) == 0 or len(email_txt) == 0 or len(password_txt) == 0:
        messagebox.showerror(
            title="Oh no...", message="Please dont leave any fields empty! ")

    else:
        # Ask the user if he wants to save the details he entered into a txt file
        is_ok = messagebox.askokcancel(
            title=website_txt, message=f"These are the details you entered:\nEmail: {email_txt}\nPassword: {password_txt}\nDo you want to save those details?")
        if is_ok:
            # Insert the data into a txt file
            with open("data.txt", "a") as data_file:
                # Save the data that the use entered
                data_file.write(
                    f"{website_txt} | {email_txt} | {password_txt}\n")

    # Clear the Entrys
    website_entry.delete(0, "end")
    email_entry.delete(0, "end")
    password_entry.delete(0, "end")

# ----------------------------------------Password Generate-----------------------------------------


def generate_password():
    # Delete the password in password_entry every time the user press the add button
    password_entry.delete(0, "end")
    password_list = []
    password = ""
    # Creating small letters list with 6 chars
    small_letters_list = [random.choice(small_letters) for _ in range(6)]
    # Creating big letters list with 2 chars
    big_letters_list = [random.choice(big_letters) for _ in range(2)]
    # Creating numbers list with 5 chars
    numbers_list = [random.choice(numbers) for _ in range(5)]
    # Creating symbols list with 3 chars
    symbols_lit = [random.choice(symbols) for _ in range(3)]
    # Creating the password list from all the lists above
    password_list = small_letters_list + big_letters_list + numbers_list + symbols_lit
    # Shuffle the list
    random.shuffle(password_list)
    # Creating the final password
    password = "".join(password_list)
    # Insert the password into the password_entry
    password_entry.insert(0, password)
    # Let the user to copy the random password immediately
    pyperclip.copy(password)


# ------------------------------------Labels, Buttons and Entrys-------------------------------------


# Labels
# Creating the Website Label
website_label = Label(text="Website:", width=20,
                      font=LABEL_FONT, fg=LABEL_FG, bg=BG)
website_label.grid(row=1, column=0, sticky="w", pady=10)
# Creating the email Label
email_label = Label(text="Email:", width=20,
                    font=LABEL_FONT, fg=LABEL_FG, bg=BG)
email_label.grid(row=2, column=0, columnspan=2, sticky="w", pady=10)
# Creating the password Label
password_label = Label(text="Password:", width=20,
                       font=LABEL_FONT, fg=LABEL_FG, bg=BG)
password_label.grid(row=3, column=0, columnspan=2, sticky="w", pady=10)

# --------------------

# Entrys
# Creating the Website Entry
website_entry = Entry(width=40, font=ENTRY_FONT)
website_entry.grid(row=1, column=1, columnspan=2, sticky='w')
website_entry.focus()
# Creating the Email Entry
email_entry = Entry(width=40, font=ENTRY_FONT)
email_entry.grid(row=2, column=1, columnspan=2, sticky='w')
# Creating the password Entry
password_entry = Entry(width=18, font=ENTRY_FONT)
password_entry.grid(row=3, column=1, columnspan=2, sticky='w')

# --------------------
# Buttons

# Creating the add button
add_button = Button(text="Add",font=ENTRY_FONT ,width=35, command=save_data_txt)
add_button.grid(row=4, column=1, columnspan=2, sticky='w')
# Creating the generate password button
generate_password_button = Button(
    text="Generate Password", font=ENTRY_FONT, width=17, command=generate_password)
generate_password_button.grid(row=3, column=1, padx=180)


window.mainloop()
