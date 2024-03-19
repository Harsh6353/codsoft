import string as st
import random 
import sys
from tkinter import *
from tkinter import messagebox


root = Tk()
root.title("Random password Generator")
root.geometry("400x500")


# generating password
def new_rand():
    #clear Input Box
    pw.delete(0,END)
    
    try:
    # Ask lengh of password
        passlen = int(pw_input.get())
        
        #creating password
        lowercase = st.ascii_lowercase
        uppercase = st.ascii_uppercase
        digits = st.digits
        symbols = st.punctuation
        #this gives set of lowercase,uppercase,digits,punctuation
        s = []
        s.extend(list(lowercase))
        s.extend(list(uppercase))
        s.extend(list(digits))
        s.extend(list(symbols))
        random.shuffle(s) #suffles set in randomise way
        password = "".join(s[0:passlen])
    
        # printing output
        pw.insert(0,password)
        password = ""
        
    except:
        #Display error message if userd enter value other than ineger
        messagebox.showerror("Error","Please enter a valid integer for password length")
    

# copy to clipboard
def copy():
    root.clipboard_clear()
    root.clipboard_append(pw.get())
    messagebox.showinfo("Copied", "Password copied to clipboard successfully!")


#Lable 
lf = LabelFrame(root,text="Enter the password length")
lf.pack(pady=20)
pw_input = Entry(lf,font=("Helvetica",25))
pw_input.pack(pady = 20, padx = 20)

# lable for output
of= LabelFrame(root,text="Your Output")
of.pack(pady=20)
pw = Entry(of , text = "",font=("Helvetica",25),bd=0)
pw.pack(pady = 20)


#creating buttons
frame = Frame(root)
frame.pack(pady=20)

button =  Button(frame, text="Generate Strong Password", command=new_rand)
button.grid(row=0,column=0,padx=10)

copy_btn = Button(frame,text = "Copy To Clipboard", command= copy)
copy_btn.grid(row = 0, column=1,padx=10)

root.mainloop()

