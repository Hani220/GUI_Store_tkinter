import json
import tkinter as tk

from tkinter import messagebox
#hanyouf37@gmail.com 0000
from login_page import LoginPage
from register_page import RegisterPage
from home_page import HomePage
from Categories_pages import CategoryPage
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("HJS Store App")
        self.root.geometry("500x500")
        self.pages = []
        self.page_stack = []
        self.load_user_data()

        self.initialize_pages()

        self.show_page("LoginPage")  # Show the "LoginPage"



    def load_user_data(self):
        try:
            with open("users.json", "r") as file:
                self.users = json.load(file)
        except FileNotFoundError:
            self.users = {}

    def save_user_data(self):
        with open("users.json", "w") as file:
            json.dump(self.users, file, indent=2)

    def add_page(self, page_class, page_instance):
        self.pages.append((page_class, page_instance))

    def initialize_pages(self):
        self.login_page = LoginPage(self.root, self)
        self.register_page = RegisterPage(self.root, self)
        self.home_page = HomePage(self.root, self)

        self.add_page(LoginPage, self.login_page)
        self.add_page(RegisterPage, self.register_page)
        self.add_page(HomePage, self.home_page)

        self.sports_page = CategoryPage(self.root, self, "Sports")
        self.appliances_page = CategoryPage(self.root, self, "Home appliances")
        self.electronics_page = CategoryPage(self.root, self, "Electronics")
        self.fashion_page = CategoryPage(self.root, self, "Fashion")
        self.books_page = CategoryPage(self.root, self, "Books")

        self.add_page(CategoryPage, self.sports_page)
        self.add_page(CategoryPage, self.appliances_page)
        self.add_page(CategoryPage, self.electronics_page)
        self.add_page(CategoryPage, self.fashion_page)
        self.add_page(CategoryPage, self.books_page)

    def show_page(self, page_name):
            for page_class, page_instance in self.pages:
                if page_class.__name__ == page_name:
                    if self.page_stack:
                        previous_page = self.page_stack[-1]
                        previous_page.pack_forget()
                    page_instance.pack()
                    self.page_stack.append(page_instance)
                    break

    def show_previous_page(self):
        if len(self.page_stack) > 1:
            self.page_stack.pop().pack_forget()
            previous_page = self.page_stack[-1]
            previous_page.pack()


root = tk.Tk()
app = App(root)
root.mainloop()