import tkinter as tk
from tkinter import ttk, messagebox
import csv

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")

        self.contacts = []

        # Create GUI elements with styling
        style = ttk.Style()
        style.configure("TLabel", font=("Helvetica", 12))
        style.configure("TButton", font=("Helvetica", 12))

        self.label_name = ttk.Label(root, text="Name:")
        self.label_name.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.entry_name = ttk.Entry(root, width=30)
        self.entry_name.grid(row=0, column=1, padx=10, pady=10)

        self.label_number = ttk.Label(root, text="Number:")
        self.label_number.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.entry_number = ttk.Entry(root, width=30)
        self.entry_number.grid(row=1, column=1, padx=10, pady=10)

        self.label_email = ttk.Label(root, text="Email:")
        self.label_email.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.entry_email = ttk.Entry(root, width=30)
        self.entry_email.grid(row=2, column=1, padx=10, pady=10)

        self.button_save = ttk.Button(root, text="Save", command=self.save_contact)
        self.button_save.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.button_search = ttk.Button(root, text="Search", command=self.search_contact)
        self.button_search.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        self.button_show_all = ttk.Button(root, text="Show All", command=self.show_all_contacts)
        self.button_show_all.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        self.tree = ttk.Treeview(root, columns=("Name", "Number", "Email"), show="headings")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Number", text="Number")
        self.tree.heading("Email", text="Email")
        self.tree.grid(row=6, column=0, columnspan=2, padx=10, pady=10)
        self.tree.bind("<Double-1>", self.edit_contact)

        self.button_delete = ttk.Button(root, text="Delete", command=self.delete_contact)
        self.button_delete.grid(row=7, column=0, columnspan=2, padx=10, pady=10)
        
        self.button_delete = ttk.Button(root, text="Edit", command=self.edit_contact)
        self.button_delete.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

        self.load_contacts()


    #function to save contacts
    def save_contact(self):
        name = self.entry_name.get()
        number = self.entry_number.get()
        email = self.entry_email.get()

        if name.lower() in [contact["Name"].lower() for contact in self.contacts]:
            messagebox.showerror("Error", "Contact with the same name already exists.")
        elif name and number and email:
            contact = {"Name": name, "Number": number, "Email": email}
            self.contacts.append(contact)
            self.save_to_csv(contact)
            messagebox.showinfo("Success", "Contact saved successfully.")
            self.clear_entries()
            self.load_contacts()
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    # functuon to save contact to csv file 
    def save_to_csv(self, contact):
        with open("C:\codsoft\codsoft\contact_book\contacts.csv", mode="a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["Name", "Number", "Email"])
            if file.tell() == 0:
                writer.writeheader()
            writer.writerow(contact)

    # fun to load contacts 
    def load_contacts(self):
        self.contacts.clear()
        self.tree.delete(*self.tree.get_children())
        with open("C:\codsoft\codsoft\contact_book\contacts.csv", mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.contacts.append(row)
                self.tree.insert("", "end", values=(row["Name"], row["Number"], row["Email"]))

    # fun to search contact 
    def search_contact(self):
        search_term = self.entry_name.get()
        if search_term:
            found = False
            for contact in self.contacts:
                if contact["Name"].lower() == search_term.lower():
                    messagebox.showinfo("Contact Found", f"Name: {contact['Name']}\nNumber: {contact['Number']}\nEmail: {contact['Email']}")
                    found = True
                    break
            if not found:
                messagebox.showinfo("Contact Not Found", "No contact found with that name.")
        else:
            messagebox.showerror("Error", "Please enter a name to search.")

    # fun to edit contact 
    def edit_contact(self,event=None):
        item = self.tree.focus()
        if item:
            contact = self.contacts[self.tree.index(item)]
            edit_window = tk.Toplevel()
            edit_window.title("Edit Contact")

            ttk.Label(edit_window, text="Name:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
            ttk.Label(edit_window, text="Number:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
            ttk.Label(edit_window, text="Email:").grid(row=2, column=0, padx=10, pady=10, sticky="w")

            entry_name = ttk.Entry(edit_window, width=30)
            entry_name.grid(row=0, column=1, padx=10, pady=10)
            entry_name.insert(0, contact["Name"])

            entry_number = ttk.Entry(edit_window, width=30)
            entry_number.grid(row=1, column=1, padx=10, pady=10)
            entry_number.insert(0, contact["Number"])

            entry_email = ttk.Entry(edit_window, width=30)
            entry_email.grid(row=2, column=1, padx=10, pady=10)
            entry_email.insert(0, contact["Email"])
            
            def save_edit():
                new_name = entry_name.get()
                if new_name.lower() != contact["Name"].lower() and new_name.lower() in [c["Name"].lower() for c in self.contacts]:
                    messagebox.showerror("Error", "Contact with the same name already exists.")
                else:
                    contact["Name"] = new_name
                    contact["Number"] = entry_number.get()
                    contact["Email"] = entry_email.get()
                    self.save_all_contacts_to_csv()
                    edit_window.destroy()
                    self.load_contacts()

            ttk.Button(edit_window, text="Save", command=save_edit).grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        else:
            messagebox.showerror("Error", "Please select a contact to edit.")

    # fun to delete contact 
    def delete_contact(self):
        item = self.tree.focus()
        if item:
            index = self.tree.index(item)
            del self.contacts[index]
            self.tree.delete(item)
            self.save_all_contacts_to_csv()
        else:
            messagebox.showerror("Error", "Please select a contact to delete.")

    def save_all_contacts_to_csv(self):
        with open("C:\codsoft\codsoft\contact_book\contacts.csv", mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["Name", "Number", "Email"])
            writer.writeheader()
            for contact in self.contacts:
                writer.writerow(contact)

    def show_all_contacts(self):
        messagebox.showinfo("All Contacts", "\n".join([f"Name: {contact['Name']}\nNumber: {contact['Number']}\nEmail: {contact['Email']}" for contact in self.contacts]))

    def clear_entries(self):
        self.entry_name.delete(0, tk.END)
        self.entry_number.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    contact_book = ContactBook(root)
    root.mainloop()
