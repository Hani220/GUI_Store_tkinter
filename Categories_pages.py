import tkinter as tk

class CategoryPage(tk.Frame):
    def __init__(self, root, app, category):
        tk.Frame.__init__(self, root)
        self.root = root
        self.app = app
        self.category = category
        self.create_widgets()

    def create_widgets(self):
        self.search_label = tk.Label(self, text="Search:")
        self.search_label.grid(row=0, column=0)

        self.search_entry = tk.Entry(self)
        self.search_entry.grid(row=0, column=1)

        self.add_to_cart_button = tk.Button(self, text="Add to Cart", command=self.add_to_cart)
        self.add_to_cart_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        self.sort_asc_button = tk.Button(self, text="Sort Ascending", command=self.sort_ascending)
        self.sort_asc_button.grid(row=2, column=0, padx=5, pady=5)

        self.sort_desc_button = tk.Button(self, text="Sort Descending", command=self.sort_descending)
        self.sort_desc_button.grid(row=2, column=1, padx=5, pady=5)

        self.back_button = tk.Button(self, text="Back", command=self.go_back, bg="red")
        self.back_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    def sort_ascending(self):
        self.category.sort(key=lambda item: item.price)
        print("Sorted in ascending order")

    def sort_descending(self):
        self.category.sort(key=lambda item: item.price, reverse=True)
        print("Sorted in descending order")

    def add_to_cart(self):
        print("Add to Cart button clicked")


    def go_back(self):
        self.app.show_previous_page()
