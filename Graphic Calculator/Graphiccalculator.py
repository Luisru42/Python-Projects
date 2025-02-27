import tkinter as tk
from tkinter import ttk

# Define the Calculator class
class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("350x400")

        # Initialize the expression to be evaluated
        self.expression = ""
        self.input_text = tk.StringVar()

        # Create the widgets (input field and buttons)
        self.create_widgets()

    def create_widgets(self):
        # Create a frame for the input field
        input_frame = ttk.Frame(self.root, padding="10")
        input_frame.pack(expand=True, fill="both")

        # Create the input field where the expression is displayed
        input_field = ttk.Entry(input_frame, textvariable=self.input_text, font=('arial', 18, 'bold'), justify='right')
        input_field.pack(expand=True, fill="both")

        # Create a frame for the buttons
        button_frame = ttk.Frame(self.root)
        button_frame.pack(expand=True, fill="both")

        # List of button labels
        buttons = [
            '7', '8', '9', '/', 
            '4', '5', '6', '*', 
            '1', '2', '3', '-', 
            'C', '0', '=', '+'
        ]

        # Initialize row and column indices for button placement
        row = 0
        col = 0

        # Create buttons and place them in the grid
        for button in buttons:
            # Create a button and assign its click event
            action = lambda x=button: self.click_event(x)
            ttk.Button(button_frame, text=button, command=action).grid(row=row, column=col, sticky="nsew")

            # Move to the next column
            col += 1
            if col > 3:  # Move to the next row after every 4th button
                col = 0
                row += 1

        # Configure grid layout for uniform button sizes
        for i in range(4):
            button_frame.grid_columnconfigure(i, weight=1)
            button_frame.grid_rowconfigure(i, weight=1)

    def click_event(self, button):
        if button == 'C':
            # Clear the expression if 'C' is pressed
            self.expression = ""
        elif button == '=':
            try:
                # Evaluate the expression if '=' is pressed
                self.expression = str(eval(self.expression))
            except:
                # Display an error message if the evaluation fails
                self.expression = "Error"
        else:
            # Append the button text to the expression
            self.expression += button
        
        # Update the input field with the current expression
        self.input_text.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
