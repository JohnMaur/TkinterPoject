from tkinter import Label, Button, messagebox

class HomeController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.frame = self.view.frames["home"]
        self.checkout_items = []  # List to store checkout items
        self.history_items = []   # List to store history items
        self._bind()
        self.checkout_items_fetched = False  # Flag to track if checkout items have been fetched
        self.fetch_and_display_checkout_items()  # Fetch and display checkout items on initialization

    def fetch_and_display_checkout_items(self):
        if not self.checkout_items_fetched:  # Check if checkout items have not been fetched yet
            if self.model.auth.is_logged_in and self.model.auth.current_user:
                user_id = self.model.auth.current_user.get("userID")
                if user_id is not None:
                    checkout_items = self.model.auth.fetch_checkout_items(user_id)
                    if checkout_items:
                        for item_name, item_price in checkout_items:
                            # Display the fetched items without adding them to the checkout list
                            self.display_checkout_item(item_name, item_price)
                    else:
                        messagebox.showinfo("Checkout Empty", "Your checkout is empty.")
                else:
                    print("User ID is not available.")
                self.checkout_items_fetched = True  # Set the flag to True after fetching items
            else:
                print("No user is currently logged in.")

    def display_checkout_item(self, item_name, item_price):
        # Create labels for name and price
        name_label = Label(self.frame.checkout_frame, text=item_name, bg="white", font=("", 9, "bold"))
        price_label = Label(self.frame.checkout_frame, text=item_price, bg="white", fg="orange", font=("", 9, "bold"))

        # Grid the labels
        name_label.grid(row=len(self.frame.checkout_frame.grid_slaves()) + 1, column=0, sticky="w", padx=15)
        price_label.grid(row=len(self.frame.checkout_frame.grid_slaves()) + 1, column=0, sticky="w", padx=15)

        # Create buttons for removing and buying
        buy_button = Button(self.frame.checkout_frame, text="Buy", bg="green", fg="white", font=("", 8, "bold"),
                            command=lambda: self.move_to_history(item_name, item_price, name_label, price_label,
                                                                 buy_button, remove_button))
        remove_button = Button(self.frame.checkout_frame, text="Remove", bg="red", fg="white", font=("", 8, "bold"),
                               command=lambda: self.remove_item(item_name, item_price, name_label, price_label,
                                                                remove_button, buy_button))

        # Grid the buttons
        buy_button.grid(row=len(self.frame.checkout_frame.grid_slaves()) + 1, column=0, sticky="w", padx=15, pady=2)
        remove_button.grid(row=len(self.frame.checkout_frame.grid_slaves()) + 1, column=0, sticky="w", padx=15, pady=2)


    def _bind(self):
        self.frame.signout_btn.config(command=self.logout)
        self.frame.cheese_pizza_add_button.config(
            command=lambda: self.add_item_to_checkout("Cheese & Tomato Pizza", "$40.40"))
        # Add similar bindings for other add buttons

        self.frame.egg_bacon_add_button.config(
            command=lambda: self.add_item_to_checkout("Poached Egg & Bacon", "$60.45"))
        self.frame.ham_cheese_add_button.config(
            command=lambda: self.add_item_to_checkout("Smoky Ham & Cheese", "$10.00"))
        self.frame.vegan_meetball_add_button.config(
            command=lambda: self.add_item_to_checkout("Vegan Meatball Wrap", "$35.00"))
        self.frame.vegan_bbq_add_button.config(
            command=lambda: self.add_item_to_checkout("Vegan BBQ Chick'n Panini", "$35.00"))
        self.frame.creamy_mac_add_button.config(
            command=lambda: self.add_item_to_checkout("Creamy Mac & Cheese", "$40.00"))

    def logout(self):
        self.model.auth.logout()

    def add_item_to_checkout(self, item_name, item_price):
        # Obtain the user_id from current_user attribute of Auth instance
        user_id = self.model.auth.current_user["userID"]

        # Call add_to_checkout with user_id
        self.model.auth.add_to_checkout(item_name, item_price, user_id)

        # Create labels for name and price
        name_label = Label(self.frame.checkout_frame, text=item_name, bg="white", font=("", 9, "bold"))
        price_label = Label(self.frame.checkout_frame, text=item_price, bg="white", fg="orange", font=("", 9, "bold"))

        # Grid the labels
        name_label.grid(row=len(self.frame.checkout_frame.grid_slaves()) + 1, column=0, sticky="w", padx=15)
        price_label.grid(row=len(self.frame.checkout_frame.grid_slaves()) + 1, column=0, sticky="w", padx=15)

        # Create buttons for removing and buying
        buy_button = Button(self.frame.checkout_frame, text="Buy", bg="green", fg="white", font=("", 8, "bold"),
                            command=lambda: self.move_to_history(item_name, item_price, name_label, price_label,
                                                                 buy_button, remove_button))
        remove_button = Button(self.frame.checkout_frame, text="Remove", bg="red", fg="white", font=("", 8, "bold"),
                               command=lambda: self.remove_item(item_name, item_price, name_label, price_label,
                                                                remove_button, buy_button))

        # Grid the buttons
        buy_button.grid(row=len(self.frame.checkout_frame.grid_slaves()) + 1, column=0, sticky="w", padx=15, pady=2)
        remove_button.grid(row=len(self.frame.checkout_frame.grid_slaves()) + 1, column=0, sticky="w", padx=15, pady=2)

        # Add the item to the checkout list
        self.checkout_items.append((item_name, item_price, name_label, price_label, buy_button, remove_button))

    def move_to_history(self, item_name, item_price, name_label, price_label, buy_button, remove_button):
        # Forget the buttons from the checkout frame
        name_label.grid_forget()
        price_label.grid_forget()
        remove_button.grid_forget()
        buy_button.grid_forget()

        # Grid the labels in the history frame
        Label(self.frame.history_frame, text=item_name, bg="white", font=("", 9, "bold")).grid(
            row=len(self.frame.history_frame.grid_slaves()) + 1, column=0, sticky="w", padx=15)
        Label(self.frame.history_frame, text=item_price, bg="white", fg="orange", font=("", 9, "bold")).grid(
            row=len(self.frame.history_frame.grid_slaves()) + 1, column=0, sticky="w", padx=15)

        # Add the item to the history list
        self.history_items.append((item_name, item_price))

        # Obtain the user_id from current_user attribute of Auth instance
        user_id = self.model.auth.current_user["userID"]

        # Insert the purchased item into the history table
        self.model.auth.add_to_history(item_name, item_price, user_id)

        # Remove the item from the checkout table
        self.model.auth.remove_from_checkout(item_name, item_price, user_id)

        # Display a "Purchased successfully" message
        messagebox.showinfo("Success", "Purchased successfully")

    def remove_item(self, item_name, item_price, name_label, price_label, remove_button, buy_button):
        item_name = name_label["text"]
        item_price = price_label["text"]

        name_label.grid_forget()
        price_label.grid_forget()
        remove_button.grid_forget()
        buy_button.grid_forget()

        # Remove the item from the checkout list
        self.checkout_items.remove((item_name, item_price, name_label, price_label, buy_button, remove_button))

        # Remove the item from the checkout table
        user_id = self.model.auth.current_user["userID"]
        self.model.auth.remove_from_checkout(item_name, item_price, user_id)

    def update_view(self):
        current_user = self.model.auth.current_user
        if current_user:
            username = current_user["username"]
            self.frame.greeting.config(text=f"User: {username}")
        else:
            self.frame.greeting.config(text=f"")