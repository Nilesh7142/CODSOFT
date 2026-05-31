import tkinter as tk
from tkinter import messagebox
import json
import os

DATA_FILE = "todo_list.json"

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python To-Do List")
        self.root.geometry("400x450")
        self.root.config(bg="#f0f0f0")
        
        self.tasks = self.load_tasks()
        
        # --- UI ELEMENTS ---
        # Title Label
        self.title_label = tk.Label(root, text="My Tasks", font=("Arial", 16, "bold"), bg="#f0f0f0")
        self.title_label.pack(pady=10)
        
        # Entry Box for new tasks
        self.task_entry = tk.Entry(root, font=("Arial", 12), width=28)
        self.task_entry.pack(pady=5)
        
        # Add Task Button
        self.add_btn = tk.Button(root, text="Add Task", font=("Arial", 10, "bold"), bg="#4CAF50", fg="white", width=12, command=self.add_task)
        self.add_btn.pack(pady=5)
        
        # Listbox to show tasks
        self.task_listbox = tk.Listbox(root, font=("Arial", 12), width=35, height=12, selectbackground="#a6a6a6")
        self.task_listbox.pack(pady=10)
        
        # Action Buttons Frame
        self.btn_frame = tk.Frame(root, bg="#f0f0f0")
        self.btn_frame.pack(pady=5)
        
        self.complete_btn = tk.Button(self.btn_frame, text="Mark Done", font=("Arial", 10), bg="#2196F3", fg="white", width=12, command=self.mark_done)
        self.complete_btn.grid(row=0, column=0, padx=5)
        
        self.delete_btn = tk.Button(self.btn_frame, text="Delete Task", font=("Arial", 10), bg="#f44336", fg="white", width=12, command=self.delete_task)
        self.delete_btn.grid(row=0, column=1, padx=5)
        
        # Load tasks into the listbox on startup
        self.refresh_listbox()
        
        # Auto-save when closing the window
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    # --- FUNCTIONALITY ---
    def load_tasks(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as f:
                return json.load(f)
        return []

    def save_tasks(self):
        with open(DATA_FILE, "w") as f:
            json.dump(self.tasks, f, indent=4)

    def refresh_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "[✓] " if task["done"] else "[ ] "
            self.task_listbox.insert(tk.END, status + task["title"])

    def add_task(self):
        title = self.task_entry.get().strip()
        if title:
            self.tasks.append({"title": title, "done": False})
            self.refresh_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You cannot add an empty task!")

    def mark_done(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.tasks[selected_index]["done"] = True
            self.refresh_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task first!")

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.tasks.pop(selected_index)
            self.refresh_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task first!")

    def on_closing(self):
        self.save_tasks()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()