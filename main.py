from password_generator import *
import tkinter as tk
from tkinter import messagebox
import os
import pyperclip, json

window = tk.Tk()
window.title('Password manager')
window.config(padx=50, pady=50)

# -----------------------------------------Global Variables and Functions--------------------------------------------- #

website_name = ''
email = ''
password_str = ''

if os.path.getsize('data.json') != 0:
    with open('data.json', 'r') as dat_file:
        data = json.load(dat_file)
        usual_email = data[next(iter(data))]['Email']
        email = usual_email


def clear_inputs():
    website_input.delete(0, tk.END)
    password_input.delete(0, tk.END)

# ------------------------------------------------Entry commands------------------------------------------------------ #


def handle_search():
    try:
        with open('data.json', 'r') as data_file:
            website = json.load(data_file)
            website_dict = website[website_name]

            email_input.delete(0, tk.END)
            password_input.delete(0, tk.END)
            email_input.insert(tk.END, website_dict['Email'])
            password_input.insert(tk.END, website_dict['Password'])

    except json.decoder.JSONDecodeError:
        email_input.delete(0, tk.END)
        password_input.delete(0, tk.END)
        website_input.delete(0, tk.END)
        messagebox.showerror(title='Error!', message="No data found.")


def handle_website_name(sv):
    global website_name

    website_name = sv.get()


sv_website = tk.StringVar()
sv_website.trace('w', lambda name, index, mode, sv=sv_website: handle_website_name(sv_website))


def handle_password(sv):
    global password_str

    password_str = sv.get()


sv_password = tk.StringVar()
sv_password.trace('w', lambda name, index, mode, sv=sv_password: handle_password(sv_password))


def handle_email(sv):
    global email

    email = sv.get()


sv_email = tk.StringVar(window, email)
sv_email.trace('w', lambda name, index, mode, sv=sv_email: handle_email(sv_email))

# ----------------------------------------------------Buttons--------------------------------------------------------- #


def confirm_form():
    if website_name == '' or email == '' or password_str == '':
        messagebox.showwarning(title='Waring!', message="Please, fill in all the boxes!")
        clear_inputs()

    else:
        confirmation = messagebox.askokcancel(title='Confirm?', message=f"""        Website: {website_name}
        Email: {email}
        Password: {password_str}
        
        Are you sure you want to confirm?""")

        if confirmation:
            new_data = {
                website_name: {
                    'Email': email,
                    'Password': password_str
                }
            }

            try:
                with open('data.json', 'r') as data_file:
                    old_data = json.load(data_file)
                    old_data.update(new_data)

            except json.decoder.JSONDecodeError:
                old_data = new_data

            with open('data.json', 'w') as data_file:
                json.dump(old_data, data_file, indent=4)
                clear_inputs()

        else:
            clear_inputs()


def generate_password_action():
    password = password_generator()
    password_input.delete(1, tk.END)
    password_input.insert(tk.END, password)
    pyperclip.copy(password)

# ------------------------------------------------------UI------------------------------------------------------------ #


canvas = tk.Canvas(height=200, width=200)
logo_image = tk.PhotoImage(file='logo.png')
logo = canvas.create_image(100, 100, image=logo_image, anchor='center')
canvas.grid(row=0, column=1)

website_title = tk.Label(text='Website:')
website_title.grid(row=1, column=0)
website_input = tk.Entry(window, width=21, textvariable=sv_website)
website_input.focus()
website_input.grid(row=1, column=1)

search_button = tk.Button(text='Search', width=15, command=handle_search)
search_button.grid(row=1, column=2)

email_title = tk.Label(text='Email/Username:')
email_title.grid(row=2, column=0)
email_input = tk.Entry(width=40, textvariable=sv_email, )
email_input.grid(row=2, column=1, columnspan=2)

password_title = tk.Label(text='Password:')
password_title.grid(row=3, column=0)
password_input = tk.Entry(width=21, textvariable=sv_password)
password_input.grid(row=3, column=1)
password_button = tk.Button(text='Generate Password', width=15, height=1, command=generate_password_action)
password_button.grid(row=3, column=2)

add_button = tk.Button(text='Add', width=35, command=confirm_form)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
