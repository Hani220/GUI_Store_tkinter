import tkinter as tk
from tkinter import messagebox

class RegisterPage(tk.Frame):
    def __init__(self, root, app):
        tk.Frame.__init__(self, root)
        self.root = root
        self.app = app

    def create_widgets(self):
        self.name_label = tk.Label(self, text="Name:")
        self.name_entry = tk.Entry(self)
        self.phone_label = tk.Label(self, text="Phone:")
        self.phone_entry = tk.Entry(self)
        self.gender_label = tk.Label(self, text="Gender:")
        self.gender_entry = tk.Entry(self)
        self.governorate_label = tk.Label(self, text="Governorate:")
        self.governorate_entry = tk.Entry(self)

        self.email_label = tk.Label(self, text="Email:")
        self.email_entry = tk.Entry(self)
        self.password_label = tk.Label(self, text="Password:")
        self.password_entry = tk.Entry(self, show="*")
        self.confirm_password_label = tk.Label(self, text="Confirm Password:")
        self.confirm_password_entry = tk.Entry(self, show="*")
        self.age_label = tk.Label(self, text="Age:")
        self.age_entry = tk.Entry(self)
        self.national_id_label = tk.Label(self, text="National ID:")
        self.national_id_entry = tk.Entry(self)
        self.register_button = tk.Button(self, text="Register", command=self.register,bg = "cyan")
        self.back_button = tk.Button(self, text="Back", command=self.go_back,bg="red")

        self.name_label.pack()
        self.name_entry.pack()
        self.phone_label.pack()
        self.phone_entry.pack()
        self.gender_label.pack()
        self.gender_entry.pack()
        self.governorate_label.pack()
        self.governorate_entry.pack()
        self.email_label.pack()
        self.email_entry.pack()
        self.password_label.pack()
        self.password_entry.pack()
        self.confirm_password_label.pack()
        self.confirm_password_entry.pack()
        self.age_label.pack()
        self.age_entry.pack()
        self.national_id_label.pack()
        self.national_id_entry.pack()
        self.register_button.pack()
        self.back_button.pack()

    def register(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        gender = self.gender_entry.get()
        governorate = self.governorate_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()
        age = self.age_entry.get()
        national_id = self.national_id_entry.get()

        if not name or not phone or not gender or not governorate or not email or not password or not confirm_password or not age or not national_id:
            messagebox.showerror("Error", "Please fill in all fields.")
        elif password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match.")
        elif email in self.app.users:
            messagebox.showerror("Error", "Email already registered.")
        else:
            self.app.users[email] = {
                "name": name,
                "phone": phone,
                "gender": gender,
                "governorate": governorate,
                "email": email,
                "password": password,
                "age": age,
                "national_id": national_id
            }
            self.app.save_user_data()
            messagebox.showinfo("Success", "Registration successful.")
            self.go_back()

            self.app.show_page("login")


    def go_back(self):
         self.app.show_previous_page()

