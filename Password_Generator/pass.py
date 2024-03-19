import string as st
from tkinter import *
from tkinter import messagebox
import json
import random

root = Tk()
root.title("Random password Generator")
root.geometry("400x500")

# Function to generate password
def new_rand():
    # Clear Input Box
    pw.delete(0, END)

    try:
        # Ask for password length
        passlen = int(pw_input.get())

        # Get user's name
        name = name_input.get()

        # Creating password
        lowercase = st.ascii_lowercase
        uppercase = st.ascii_uppercase
        digits = st.digits
        symbols = st.punctuation
        s = []
        s.extend(list(lowercase))
        s.extend(list(uppercase))
        s.extend(list(digits))
        s.extend(list(symbols))
        random.shuffle(s)
        password = "".join(s[0:passlen])

        # Store password in JSON file
        with open("C:\codsoft\codsoft\Password_Generator\passwords.json", 'a') as f:
            data = {name: password}
            json.dump(data, f, indent=4)

        # Print password to the output field
        pw.insert(0, password)

    except ValueError:
        # Display error message if user enters a non-integer value
        messagebox.showerror("Error", "Please enter a valid integer for password length")

# Function to copy password to clipboard
def copy():
    root.clipboard_clear()
    root.clipboard_append(name_input.get() + ": " + pw.get())
    messagebox.showinfo("Copied", "Password copied to clipboard successfully!")

# Label for user's name
name_label = Label(root, text="Enter your name:")
name_label.pack(pady=20)
name_input = Entry(root, font=("Helvetica", 12))
name_input.pack(pady=10)

# Label for password length
pw_label = Label(root, text="Enter the password length:")
pw_label.pack()

# Entry for password length
pw_input = Entry(root, font=("Helvetica", 12))
pw_input.pack()

# Label for password output
output_label = Label(root, text="Your Output:")
output_label.pack(pady=20)

# Entry for password output
pw = Entry(root, text="", font=("Helvetica", 12), bd=0)
pw.pack()

# Frame for buttons
frame = Frame(root)
frame.pack(pady=20)

# Button to generate password
generate_btn = Button(frame, text="Generate Strong Password", command=new_rand)
generate_btn.grid(row=0, column=0, padx=10)

# Button to copy password to clipboard
copy_btn = Button(frame, text="Copy To Clipboard", command=copy)
copy_btn.grid(row=0, column=1, padx=10)

root.mainloop()
