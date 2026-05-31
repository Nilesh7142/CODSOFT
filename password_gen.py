import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Secure Password Generator")
        self.root.geometry("420x400")
        self.root.config(bg="#f4f6f9")
        self.root.resizable(False, False)
        
        # --- UI ELEMENTS ---
        # Title
        tk.Label(root, text="Password Generator", font=("Arial", 16, "bold"), bg="#f4f6f9", fg="#2c3e50").pack(pady=15)
        
        # Length Slider
        tk.Label(root, text="Password Length:", font=("Arial", 10, "bold"), bg="#f4f6f9").pack()
        self.length_slider = tk.Scale(root, from_=6, to=32, orient="horizontal", length=250, bg="#f4f6f9", highlightthickness=0)
        self.length_slider.set(12) 
        self.length_slider.pack(pady=5)
        
        # Complexity Framework
        self.frame_options = tk.LabelFrame(root, text="Include Preferences", font=("Arial", 10, "bold"), bg="#f4f6f9", padx=20, pady=10)
        self.frame_options.pack(pady=10)
        
        # Boolean variables linked to checkboxes
        self.var_upper = tk.BooleanVar(value=True)
        self.var_digits = tk.BooleanVar(value=True)
        self.var_special = tk.BooleanVar(value=False)
        
        # Checkboxes
        tk.Checkbutton(self.frame_options, text="Uppercase Letters (A-Z)", variable=self.var_upper, bg="#f4f6f9").pack(anchor="w")
        tk.Checkbutton(self.frame_options, text="Numbers (0-9)", variable=self.var_digits, bg="#f4f6f9").pack(anchor="w")
        tk.Checkbutton(self.frame_options, text="Symbols (!@#$%)", variable=self.var_special, bg="#f4f6f9").pack(anchor="w")
        
        # Display Box for Generated Password
        self.password_var = tk.StringVar(value="Click Generate")
        self.password_entry = tk.Entry(root, textvariable=self.password_var, font=("Courier", 14, "bold"), width=24, justify="center", bd=2, relief="groove")
        self.password_entry.pack(pady=15)
        
        # Button Frame
        self.btn_frame = tk.Frame(root, bg="#f4f6f9")
        self.btn_frame.pack()
        
        self.gen_btn = tk.Button(self.btn_frame, text="Generate", font=("Arial", 10, "bold"), bg="#3498db", fg="white", padx=10, pady=5, command=self.generate)
        self.gen_btn.grid(row=0, column=0, padx=5)
        
        self.copy_btn = tk.Button(self.btn_frame, text="Copy", font=("Arial", 10, "bold"), bg="#2ecc71", fg="white", padx=10, pady=5, command=self.copy_to_clipboard)
        self.copy_btn.grid(row=0, column=1, padx=5)

    def generate(self):
        length = self.length_slider.get()
        pool = string.ascii_lowercase 
        
        if self.var_upper.get():
            pool += string.ascii_uppercase
        if self.var_digits.get():
            pool += string.digits
        if self.var_special.get():
            pool += string.punctuation
            
        generated = "".join(random.choice(pool) for _ in range(length))
        self.password_var.set(generated)

    def copy_to_clipboard(self):
        current_pwd = self.password_var.get()
        if current_pwd and current_pwd != "Click Generate":
            self.root.clipboard_clear()
            self.root.clipboard_append(current_pwd)
            messagebox.showinfo("Success", "Password copied to clipboard!")
        else:
            messagebox.showwarning("Error", "Generate a password first!")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()