import random
import string

import customtkinter as ctk

from tkinter import messagebox, PhotoImage

class RandomPassword:
    """A Class to manage the random password generation app"""

    def rp(self, length):
        """Generate a random password of given length"""
        # Set the Length and character sets
        self.length = length
        self.lower = string.ascii_lowercase  # Lower-Case Alphabet
        self.upper = string.ascii_uppercase  # Upper-Case Alphabet
        self.digits = string.digits  # Digits
        self.symbols = string.punctuation  # Special Characters

        # Combine all characters into one string
        self.all = self.lower + self.upper + self.digits + self.symbols

        # Return the password as string
        self.temp = random.sample(self.all, self.length)
        return "".join(self.temp)
    
    def on_click(self):
        try:
            length = int(self.input.get())  # Getting input from user
            # Ensure the length is within a valid range
            if length < 1 or length > 94:
                self.pwd_label.configure(text="")  # Clear the label if input is invalid
                messagebox.showerror("Invalid Input", "Please enter a number between 1 and 94.")  # Show an error message
            else:
                # Generate a password (if the length is valid)
                self.password = self.rp(length)
                # Display the generated password on the label
                self.pwd_label.configure(text=self.password)
        except ValueError:
            # Handle cases where the user inputs a non-integer value
            self.pwd_label.configure(text="")  # Clear the label if input is invalid
            messagebox.showerror("Invalid Input", "Invalid value! Enter a valid number.")  # Show an error message
    
    def copy_to_clipboard(self):
        """Copy the generated password to clipboard"""
        if self.password and self.password != "":  # Ensure there is a password and it's not empty
            self.win.clipboard_clear()  # clear the clipboard
            self.win.clipboard_append(self.password)  # Append the password to clipboard
        else:
            messagebox.showwarning("No Password", "Generate a password first")
    
    def copy_alert(self):
        """Show an alert when the password in copied to clipboard"""
        messagebox.showinfo("Alert", "Copied to Clipboard!")
    
    def clipboard(self):
        """Combine copy to clipboard and alert function"""
        self.copy_to_clipboard()
        self.copy_alert()

    def app(self):
        """Create the application window and set up the UI"""
        # Setting up Appearance
        ctk.set_appearance_mode("light")

        # Initialize the main window
        self.win = ctk.CTk()  # Create the main window
        self.win.geometry("300x300")  # Set the window size
        self.win.config(bg="white")  # Set the background color to white
        self.win.title("Random Password Generator")  # Set the window title
        self.win.resizable(False, False)  # Prevent resizing the window

        # Load the icon
        icon = PhotoImage(file="./Icon/icon.png")
        
        # Set the Windows Icon
        self.win.iconphoto(True, icon)
        
        # Title text
        self.label = ctk.CTkLabel(self.win, text="Random Password Generator", bg_color="white").pack(pady=10)

        # Input field for password length
        self.input = ctk.CTkEntry(self.win)
        self.input.pack(pady=10)

        # Label to display the generated password
        self.pwd_label = ctk.CTkLabel(self.win, text="", text_color="black", bg_color="white")
        self.pwd_label.pack(pady=10)

        # Button to generate the password
        self.button = ctk.CTkButton(self.win, text="Generate", command=self.on_click)
        self.button.pack(pady=10)

        # Button to copy the password to clipboard
        self.copy = ctk.CTkButton(self.win, text="Copy to Clipboard", command=self.clipboard)
        self.copy.pack(pady=10)

        # Start the app
        self.win.mainloop()
    
    def __init__(self):
        """Initialize the app and run it"""
        self.password = None 
        self.app()


root = RandomPassword()
