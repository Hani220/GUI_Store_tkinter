import tkinter as tk

class HomePage(tk.Frame):
    def __init__(self, root, app):
        tk.Frame.__init__(self, root)
        self.root = root
        self.app = app
        self.create_widgets()

    def create_widgets(self):
        self.categories = [
            "Home appliances",
            "Electronics",
            "Fashion",
            "Books",
            "Sports"
        ]

        self.category_label = tk.Label(self, text="Categories:")
        self.category_label.grid(row=0, column=0, columnspan=2)

        for i, category in enumerate(self.categories):
            row = i // 2 + 1
            column = i % 2
            category_button = tk.Button(self, text=category, command=lambda cat=category: self.category_clicked(cat),
                                        width=20, height=2, bg="purple", fg="white")
            category_button.grid(row=row, column=column, padx=5, pady=5)

        self.back_button = tk.Button(self, text="Back", command=self.go_back, width=10, height=1, bg="red", fg="white")
        self.back_button.grid(row=len(self.categories) // 2 + 2, column=0, columnspan=1, padx=5, pady=5)


    def category_clicked(self, category):
        self.app.show_page("CategoryPage")  # Show the generic "CategoryPage"

    def go_back(self):
        self.app.show_previous_page()