import tkinter as tk
from tkinter import messagebox

class LoginPage(tk.Frame):
    def __init__(self, root, app):
        tk.Frame.__init__(self, root)
        self.root = root
        self.app = app
        self.create_widgets()

    def create_widgets(self):
        self.email_label = tk.Label(self, text="Email:")
        self.email_entry = tk.Entry(self)
        self.password_label = tk.Label(self, text="Password:")
        self.password_entry = tk.Entry(self, show="*")
        self.login_button = tk.Button(self, text="Login", command=self.login, bg="purple")
        self.register_button = tk.Button(self, text="Register", command=self.register, bg="cyan")

        self.email_label.pack()
        self.email_entry.pack()
        self.password_label.pack()
        self.password_entry.pack()
        self.login_button.pack()
        self.register_button.pack()

    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()

        if email == "admin@gmail.com" and password == "admin123":
            messagebox.showinfo("Welcome", "Welcome, Administrator!")
            self.root.destroy()
        elif email in self.app.users and self.app.users[email]["password"] == password:
            name = self.app.users[email]['name']
            messagebox.showinfo("Welcome", f"Welcome back, {name} to HJS Store!")
            self.app.current_user = email  # Set the current user
            self.app.show_page("HomePage")  # Show the "HomePage"
        else:
            messagebox.showerror("Login Failed", "Invalid email or password.")

    def register(self):
        self.app.show_page("RegisterPage")
