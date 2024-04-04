import tkinter as tk
from tkinter import messagebox
import json
import csv

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        
        self.tasks = []
        
        # Task Entry
        self.task_entry = tk.Entry(root, width=30)
        self.task_entry.pack(pady=20)
        
        # Add Task Button
        self.add_task_btn = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_task_btn.pack(pady=10)
        
        # Task List
        self.task_list = tk.Listbox(root, height=10, width=50, border=0)
        self.task_list.pack(padx=20, pady=10)
        
        # Delete Task Button
        self.delete_task_btn = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_task_btn.pack(pady=10)
        
        # Mark Task Button
        self.mark_task_btn = tk.Button(root, text="Mark as Completed", command=self.mark_task)
        self.mark_task_btn.pack(pady=10)
        
        
        # Save Button
        self.save_btn = tk.Button(root, text="Save Tasks", command=self.save_tasks)
        self.save_btn.pack(pady=10)
        
        # Load Button
        self.load_btn = tk.Button(root, text="Load Tasks", command=self.load_tasks)
        self.load_btn.pack(pady=10)
        
        # Populate task list
        self.load_tasks()
    
    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.update_task_list()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")
    
    def delete_task(self):
        try:
            index = self.task_list.curselection()[0]
            del self.tasks[index]
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete.")
    
    def mark_task(self):
        try:
            index = self.task_list.curselection()[0]
            self.tasks[index]["completed"] = True
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to mark as completed.")
    

    def save_tasks(self):
        with open("C:/codsoft/codsoft/To_Do_List/tasks.json", "w") as file:
            json.dump(self.tasks, file)
    
    def load_tasks(self):
        try:
            with open("C:/codsoft/codsoft/To_Do_List/tasks.json", "r") as file:
                self.tasks = json.load(file)
                self.update_task_list()
        except FileNotFoundError:
            pass  # File does not exist yet, so just continue without loading
    
    def update_task_list(self):
        self.task_list.delete(0, tk.END)
        for task in self.tasks:
            status = "[✔]" if task["completed"] else "[ ]"
            self.task_list.insert(tk.END, f"{status} {task['task']}")


root = tk.Tk()
app = ToDoListApp(root)
root.mainloop()
