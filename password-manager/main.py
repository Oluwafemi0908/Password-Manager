from password_generator import PasswordGenerator
from tkinter import messagebox      # for popups
from tkinter import *
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password.delete(0, END)
    password_generator = PasswordGenerator().create_password()
    password.insert(END, password_generator)
    pyperclip.copy(password_generator)


# ---------------------------- SAVE PASSWORD ------------------------------- #

# def duplicate_check(file, new_account):       Not needed
#     new_account_key = ''
#     for key in new_account:
#         new_account_key = key
#     for account in file:
#         if new_account_key == account and new_account[0]['email'] == file[account][email]:
#             del file[account]
#             break

def search():
    result = True
    try:
        with open('data.json', 'r') as data_file:
            data = json.load(data_file)
        for key in data:
            if key == website.get().title():
                messagebox.showinfo(title='Search Result', message=f"Website: {key}\n"
                                                                   f"email: {data[key]['email']}\n"
                                                                   f"password: {data[key]['password']}")
                result = True
                pyperclip.copy(data[key]['password'])
            else:
                result = False
        if not result:
            messagebox.showinfo(title='Search Result', message="This account doesn't exist.")

    except FileNotFoundError:
        print("You don't have any password saved yet")


def save():
    password_dict = {
        website.get().title(): {
            'email': email.get().lower(),
            'password': password.get()
        }
    }
    #
    if len(website.get()) > 0 and len(email.get()) > 10 and len(password.get()) > 0:
        is_ok = messagebox.askokcancel(title=website.get(), message="Save Password")

        if is_ok:
            try:
                with open('data.json', 'r') as data_file:
                    data = json.load(data_file)     # Returns a dictionary
            except FileNotFoundError:     # In cases where there's no data file, or it's empty, you can't read them
                with open('data.json', 'w') as data_file:
                    json.dump(password_dict, data_file, indent=4)
                with open('data.json', 'r') as data_file:
                    data = json.load(data_file)
            else:
                data.update(password_dict)  # Updating the dictionary with new password created
            finally:
                with open('data.json', 'w') as data_file:
                    json.dump(data, data_file, indent=4)

            website.delete(0, END)
            email.delete(0, END)
            email.insert(END, '@email.com')
            password.delete(0, END)
            messagebox.showinfo(title='', message='Password saved')
            # print(passwords_dict)
    else:
        if len(website.get()) == 0:
            messagebox.showinfo(title='Error', message="Kindly enter website name")

        elif len(email.get()) <= 10:
            messagebox.showinfo(title='Error', message="Kindly enter email address")

        elif len(password.get()) == 0:
            messagebox.showinfo(title='Error', message="Kindly enter password")


def add_password():
    save()


# ---------------------------- UI SETUP ------------------------------- #

windows = Tk()
windows.title('Password Generator')
windows.config(pady=50, padx=50)
canvas = Canvas(width=200, height=200)
image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=image, )
canvas.grid(row=0, column=1)

# Creating Labels
label1 = Label(text='Website:')
label1.grid(row=1, column=0)
label2 = Label(text='Email/Username:')
label2.grid(row=2, column=0)
label3 = Label(text='Password:')
label3.grid(row=3, column=0)

# Creating Input fields
website = Entry(width=35)
website.grid(row=1, column=1)
website.focus()
email = Entry(width=53)
email.insert(END, '@email.com')
email.grid(row=2, column=1, columnspan=2)
password = Entry(width=35)
password.grid(row=3, column=1)

# Creating Buttons
search = Button(text='Search', command=search, width=14)
search.grid(row=1, column=2)
generate = Button(text='Generate Password', command=generate_password)
generate.grid(row=3, column=2)
add = Button(text='Add', command=add_password, width=45)
add.grid(row=4, column=1, columnspan=2)

windows.mainloop()
