import tkinter as tk
from tkinter import messagebox
from generator import PasswordGenerator

class PasswordGeneratorGui:
    def __init__(self, root):
        self.root = root
        self.root.title("PassGen")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        frame = tk.Frame(root, padx=10, pady=10)
        frame.pack(expand=True)

        # Label pentru lungimea la parola
        tk.Label(frame, text="Password Length:", anchor="w").grid(row=0, column=0, sticky="w", pady=2)
        self.length_entry = tk.Entry(frame, width=10)
        self.length_entry.insert(0, "16")
        self.length_entry.grid(row=0, column=1, pady=2)

        # Checkbox-uri pentru optiuni generare parola (liniile 62-76)
        self.digits_var = tk.BooleanVar(value=True)
        self.digits_check = tk.Checkbutton(frame, text="Include Digits", variable=self.digits_var)
        self.digits_check.grid(row=1, column=0, columnspan=2, sticky="w")

        self.special_var = tk.BooleanVar(value=True)
        self.special_check = tk.Checkbutton(frame, text="Include Special Characters", variable=self.special_var)
        self.special_check.grid(row=2, column=0, columnspan=2, sticky="w")

        self.upper_var = tk.BooleanVar(value=True)
        self.upper_check = tk.Checkbutton(frame, text="Include Uppercase Letters", variable=self.upper_var)
        self.upper_check.grid(row=3, column=0, columnspan=2, sticky="w")

        self.lower_var = tk.BooleanVar(value=True)
        self.lower_check = tk.Checkbutton(frame, text="Include Lowercase Letters", variable=self.lower_var)
        self.lower_check.grid(row=4, column=0, columnspan=2, sticky="w")

        # Buton pentru a genera parola
        self.generate_button = tk.Button(frame, text="Generate Password", command=self.generate_password, bg="#4CAF50", fg="white", padx=10, pady=5)
        self.generate_button.grid(row=5, column=0, columnspan=2, pady=10)

        # Campul cu parola rezultata
        self.result = tk.Entry(frame, state='readonly', width=30, font=("Arial", 12))
        self.result.grid(row=6, column=0, columnspan=2, pady=5)

        # Buton copiere
        self.copy_button = tk.Button(frame, text="Copy to Clipboard", command=self.copy_to_clipboard, bg="#2196F3", fg="white", padx=10, pady=5)
        self.copy_button.grid(row=7, column=0, columnspan=2, pady=5)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length < 8:
                messagebox.showwarning("Weak Password", "Passwords shorter than 8 characters are weak!")

            generator = PasswordGenerator(
                length=length,
                use_digits=self.digits_var.get(),
                use_special=self.special_var.get(),
                use_upper=self.upper_var.get(),
                use_lower=self.lower_var.get()
            )
            password = generator.generate()
            self.result.config(state='normal')
            self.result.delete(0, tk.END)
            self.result.insert(0, password)
            self.result.config(state='readonly')

        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number for the password length")

    def copy_to_clipboard(self):
        password = self.result.get()
        if password:
            self.root.clipboard_clear()
            self.root.clipboard_append(password)
            self.root.update()
            messagebox.showinfo("Copied", "Password copied to clipboard!")

def run():
    root = tk.Tk()
    app = PasswordGeneratorGui(root)
    root.mainloop()
