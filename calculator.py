import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("350x450")
        self.root.config(bg="#171616") # Dark theme background
        self.root.resizable(False, False)
        
        # String variable to store the current expression on screen
        self.expression = ""
        
        # --- DISPLAY SCREEN ---
        self.display_var = tk.StringVar(value="0")
        self.display = tk.Label(
            root, 
            textvariable=self.display_var, 
            font=("Arial", 30), 
            bg="#171616", 
            fg="#ffffff", 
            anchor="e", # Align text to the right
            padx=15, 
            pady=20
        )
        self.display.pack(expand=True, fill="both")
        
        # --- BUTTON LAYOUT ---
        # Grid layout configuration
        self.buttons_frame = tk.Frame(root, bg="#171616")
        self.buttons_frame.pack(expand=True, fill="both")
        
        # Configure rows and columns to stretch evenly
        for i in range(5):
            self.buttons_frame.rowconfigure(i, weight=1)
        for i in range(4):
            self.buttons_frame.columnconfigure(i, weight=1)
            
        # Define button labels and their positions
        button_layout = [
            ('C', 0, 0), ('(', 0, 1), (')', 0, 2), ('/', 0, 3),
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('*', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('+', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2) # '=' will span 2 columns
        ]
        
        self.create_buttons(button_layout)

    def create_buttons(self, layout):
        for (text, row, col) in layout:
            # Customize button colors based on their function
            if text == 'C':
                bg_color = "#a5a5a5"
                fg_color = "#000000"
            elif text in ['/', '*', '-', '+', '=']:
                bg_color = "#ff9f0a" # Orange for operators
                fg_color = "#ffffff"
            else:
                bg_color = "#333333" # Dark gray for numbers
                fg_color = "#ffffff"
                
            # Special case: Make the '=' button stretch over 2 columns
            colspan = 2 if text == '=' else 1
            
            btn = tk.Button(
                self.buttons_frame, 
                text=text, 
                font=("Arial", 18), 
                bg=bg_color, 
                fg=fg_color, 
                borderwidth=0, 
                relief="flat",
                command=lambda t=text: self.on_button_click(t)
            )
            btn.grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=2, pady=2)

    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
            self.display_var.set("0")
            
        elif char == '=':
            try:
                # eval handles mathematical operation string parsing perfectly
                # It evaluates something like "5+3*2" automatically using order of operations
                result = str(eval(self.expression))
                self.display_var.set(result)
                self.expression = result # Keep the result for further operations
            except ZeroDivisionError:
                self.display_var.set("Error: / by 0")
                self.expression = ""
            except Exception:
                self.display_var.set("Error")
                self.expression = ""
                
        else:
            # If the screen currently shows 0 or an error, replace it on new input
            if self.display_var.get() in ["0", "Error", "Error: / by 0"]:
                if char in ['/', '*', '-', '+']: # unless it's a starting operator
                    self.expression = "0" + char
                else:
                    self.expression = char
            else:
                self.expression += char
                
            self.display_var.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()