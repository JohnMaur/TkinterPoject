from tkinter import Frame, Label, Button, Listbox, Scrollbar, messagebox, PhotoImage, Canvas
from customtkinter import CTkLabel, CTkImage
from PIL import Image, ImageTk
import os

class HomeView(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Create header frame
        self.header_frame = Frame(self, bg="white", height=60)
        self.header_frame.place(x=0, y=0, relwidth=1)  # Adjusted placement using relative coordinates

        # Create nav frame
        self.nav_frame = Frame(self, bg="#E0E0E0", bd=1, relief="solid")
        self.nav_frame.place(x=0, y=60, relheight=1, width=150)

        # Create 2nd nav frame
        self.nav2_frame = Frame(self, bg="white", bd=0.5, relief="solid")
        self.nav2_frame.place(x=149, y=60, relheight=1, width=75)

        # Create content frame
        self.content_frame = Frame(self, bg="#E0E0E0", bd=1, relief="solid")
        self.content_frame.place(x=223, y=60, relheight=1, relwidth=1)

# ============================================== Content Frame =========================================================
        # Create Food frame
        self.food1_frame = Frame(self.content_frame, bg="#E0E0E0")
        self.food1_frame.place(x=10, y=10, height=580, width=605)

        # # Create Food frame
        # self.checkout_frame = Frame(self.content_frame, bg="white")
        # self.checkout_frame.place(x=620, y=30, height=260, width=420)


        # # Create Food frame
        # self.history_frame = Frame(self.content_frame, bg="white")
        # self.history_frame.place(x=620, y=310, height=260, width=420)

        # Create checkout canvas
        self.checkout_canvas = Canvas(self.content_frame, bg="white", highlightthickness=0)
        self.checkout_canvas.place(x=620, y=30, height=260, width=420)

        # Create checkout frame inside the canvas
        self.checkout_frame = Frame(self.checkout_canvas, bg="white")
        self.checkout_canvas.create_window((0, 0), window=self.checkout_frame, anchor='nw')

        # Add scrollbars to the canvas
        self.checkout_scrollbar = Scrollbar(self.content_frame, orient="vertical", command=self.checkout_canvas.yview)
        self.checkout_scrollbar.place(x=1035, y=30, height=260)
        self.checkout_canvas.config(yscrollcommand=self.checkout_scrollbar.set)

        # Configure canvas scroll region
        self.checkout_frame.bind("<Configure>", lambda e: self.checkout_canvas.configure(
            scrollregion=self.checkout_canvas.bbox("all")))

        # Create history canvas
        self.history_canvas = Canvas(self.content_frame, bg="white", highlightthickness=0)
        self.history_canvas.place(x=620, y=310, height=260, width=420)

        # Create history frame inside the canvas
        self.history_frame = Frame(self.history_canvas, bg="white")
        self.history_canvas.create_window((0, 0), window=self.history_frame, anchor='nw')

        # Add scrollbars to the canvas
        self.history_scrollbar = Scrollbar(self.content_frame, orient="vertical", command=self.history_canvas.yview)
        self.history_scrollbar.place(x=1035, y=310, height=260)
        self.history_canvas.config(yscrollcommand=self.history_scrollbar.set)

        # Configure canvas scroll region
        self.history_frame.bind("<Configure>",
                                lambda e: self.history_canvas.configure(scrollregion=self.history_canvas.bbox("all")))
# ============================================== Food Frame =========================================================
        # Create Food frame
        self.cheese_pizza_frame = Frame(self.food1_frame, bg="white", bd=0.5)
        self.cheese_pizza_frame.place(x=20, y=20, height=260, width=175)

        # Create Food frame
        self.egg_bacon_frame = Frame(self.food1_frame, bg="white", bd=0.5)
        self.egg_bacon_frame.place(x=215, y=20, height=260, width=175)

        # Create Food frame
        self.ham_cheese_frame = Frame(self.food1_frame, bg="white", bd=0.5)
        self.ham_cheese_frame.place(x=410, y=20, height=260, width=175)

        # Create Food frame
        self.vegan_meetball_frame = Frame(self.food1_frame, bg="white", bd=0.5)
        self.vegan_meetball_frame.place(x=20, y=300, height=260, width=175)

        # Create Food frame
        self.vegan_bbq_frame = Frame(self.food1_frame, bg="white", bd=0.5)
        self.vegan_bbq_frame.place(x=215, y=300, height=260, width=175)

        # Create Food frame
        self.creamy_mac_frame = Frame(self.food1_frame, bg="white", bd=0.5)
        self.creamy_mac_frame.place(x=410, y=300, height=260, width=175)

# ============================================== Current Content =======================================================
        # Add content to the nav frame
        self.greeting = Label(self.nav_frame, text="Welcome to Point of Sale", bg="#DDDDDD", font=("", 10, "bold"))
        self.greeting.place(relx=0.5, y=20, anchor="center")  # Adjusted placement using anchor

        self.signout_btn = Button(self.nav_frame, text="Sign Out", width=12)
        self.signout_btn.place(relx=0.5, rely=0.86, anchor="center")  # Adjusted placement using anchor

        # Add logo to the header
        logo_directory = os.path.dirname(__file__)
        logo_path = os.path.join(logo_directory, "../images/Logo.png")

        if os.path.exists(logo_path):
            self.logo_img = PhotoImage(file=logo_path)
            self.logo_label = Label(self.header_frame, image=self.logo_img, bg="white")
            self.logo_label.place(x=10, y=10)  # Adjusted placement using pack
        else:
            print("Image file not found at path:", logo_path)

        # Header text
        self.header_text = Label(self.header_frame, text="P  O  I N  T   OF   S  A  L  E", bg="white",
                                             font=("Helvetica", 18, "bold"))
        self.header_text.place(x=500, y=12)

# ======================================== 2nd Nav Bar ============================================================
        coffee_directory = os.path.dirname(__file__)
        coffee_path = os.path.join(coffee_directory, "../images/coffee.png")

        # Load and display background image
        self.coffee = CTkImage(dark_image=Image.open(coffee_path), size=(20, 20))
        self.coffee = CTkLabel(self.nav2_frame, image=self.coffee, compound="top", text="Food")
        self.coffee.grid(row=0, column=0, pady=15, padx=25)

        beverage_directory = os.path.dirname(__file__)
        beverage_path = os.path.join(beverage_directory, "../images/beverage.png")

        # Load and display background image
        self.beverage = CTkImage(dark_image=Image.open(beverage_path), size=(20, 20))
        self.beverage = CTkLabel(self.nav2_frame, image=self.beverage, compound="top", text="Beverage")
        self.beverage.grid(row=1, column=0, pady=15)

        food_directory = os.path.dirname(__file__)
        food_path = os.path.join(food_directory, "../images/food.png")

        # Load and display background image
        self.food = CTkImage(dark_image=Image.open(food_path), size=(20, 20))
        self.food = CTkLabel(self.nav2_frame, image=self.food, compound="top", text="Food")
        self.food.grid(row=2, column=0, pady=15)

        appetizer_directory = os.path.dirname(__file__)
        appetizer_path = os.path.join(appetizer_directory, "../images/appetizer.png")

        # Load and display background image
        self.appetizer = CTkImage(dark_image=Image.open(appetizer_path), size=(20, 20))
        self.appetizer = CTkLabel(self.nav2_frame, image=self.appetizer, compound="top", text="Appetizer")
        self.appetizer.grid(row=3, column=0, pady=15)

        bread_directory = os.path.dirname(__file__)
        bread_path = os.path.join(bread_directory, "../images/bread.png")

        # Load and display background image
        self.bread = CTkImage(dark_image=Image.open(bread_path), size=(20, 20))
        self.bread = CTkLabel(self.nav2_frame, image=self.bread, compound="top", text="Bread")
        self.bread.grid(row=4, column=0, pady=15)

# ======================================== Conveinient Store ===========================================================

        cheese_pizza_directory = os.path.dirname(__file__)
        cheese_pizza_directory_path = os.path.join(cheese_pizza_directory, "../images/cheese_pizza.png")

        # Load and display background image
        self.cheese_pizza = CTkImage(dark_image=Image.open(cheese_pizza_directory_path), size=(150, 150))
        self.cheese_pizza = CTkLabel(self.cheese_pizza_frame, image=self.cheese_pizza, text="")
        self.cheese_pizza.grid(row=0, column=0, padx=15)

        # Create labels for name, price, and value
        self.cheese_pizza_name_label = Label(self.cheese_pizza_frame, text="Cheese & Tomato Pizza", bg="white", font=("", 9, "bold"))
        self.cheese_pizza_name_label.grid(row=1, column=0, pady=(0, 0))

        self.cheese_pizza_price_label = Label(self.cheese_pizza_frame, text="Price", bg="white", foreground="#9C9C9C")
        self.cheese_pizza_price_label.grid(row=2, column=0, pady=(0, 0))

        self.cheese_pizza_value_label = Label(self.cheese_pizza_frame, text="$ 40.40", bg="white", fg="orange", font=("", 9, "bold"))
        self.cheese_pizza_value_label.grid(row=3, column=0, pady=(0, 0))

        self.cheese_pizza_add_button = Button(self.cheese_pizza_frame, text="ADD", bg="#F6B100", height=1, width=15,
                                 highlightthickness=0, borderwidth=0, font=("", 8, "bold"))
        self.cheese_pizza_add_button.grid(row=4, column=0, pady=(8, 0), ipady=4)

        egg_bacon_directory = os.path.dirname(__file__)
        egg_bacon_directory_path = os.path.join(egg_bacon_directory, "../images/egg_bacon.png")

        # Load and display background image
        self.egg_bacon = CTkImage(dark_image=Image.open(egg_bacon_directory_path), size=(150, 150))
        self.egg_bacon = CTkLabel(self.egg_bacon_frame, image=self.egg_bacon, text="")
        self.egg_bacon.grid(row=0, column=0, padx=15)

        # Create labels for name, price, and value
        self.egg_bacon_name_label = Label(self.egg_bacon_frame, text="Poache Egg & Bacon", bg="white",
                                             font=("", 9, "bold"))
        self.egg_bacon_name_label.grid(row=1, column=0, pady=(0, 0))

        self.egg_bacon_price_label = Label(self.egg_bacon_frame, text="Price", bg="white", foreground="#9C9C9C")
        self.egg_bacon_price_label.grid(row=2, column=0, pady=(0, 0))

        self.egg_bacon_value_label = Label(self.egg_bacon_frame, text="$ 60.45", bg="white", fg="orange",
                                              font=("", 9, "bold"))
        self.egg_bacon_value_label.grid(row=3, column=0, pady=(0, 0))

        self.egg_bacon_add_button = Button(self.egg_bacon_frame, text="ADD", bg="#F6B100", height=1, width=15,
                                              highlightthickness=0, borderwidth=0, font=("", 8, "bold"))
        self.egg_bacon_add_button.grid(row=4, column=0, pady=(8, 0), ipady=4)

        ham_cheese_directory = os.path.dirname(__file__)
        ham_cheese_directory_path = os.path.join(ham_cheese_directory, "../images/ham_cheese.png")

        # Load and display background image
        self.ham_cheese = CTkImage(dark_image=Image.open(ham_cheese_directory_path), size=(150, 150))
        self.ham_cheese = CTkLabel(self.ham_cheese_frame, image=self.ham_cheese, text="")
        self.ham_cheese.grid(row=0, column=0, padx=15)

        # Create labels for name, price, and value
        self.ham_cheese_name_label = Label(self.ham_cheese_frame, text="Smoky Ham & Cheese", bg="white",
                                             font=("", 9, "bold"))
        self.ham_cheese_name_label.grid(row=1, column=0, pady=(0, 0))

        self.ham_cheese_price_label = Label(self.ham_cheese_frame, text="Price", bg="white", foreground="#9C9C9C")
        self.ham_cheese_price_label.grid(row=2, column=0, pady=(0, 0))

        self.ham_cheese_value_label = Label(self.ham_cheese_frame, text="$ 10.00", bg="white", fg="orange",
                                              font=("", 9, "bold"))
        self.ham_cheese_value_label.grid(row=3, column=0, pady=(0, 0))

        self.ham_cheese_add_button = Button(self.ham_cheese_frame, text="ADD", bg="#F6B100", height=1, width=15,
                                              highlightthickness=0, borderwidth=0, font=("", 8, "bold"))
        self.ham_cheese_add_button.grid(row=4, column=0, pady=(8, 0), ipady=4)

        vegan_meetball_directory = os.path.dirname(__file__)
        vegan_meetball_directory_path = os.path.join(vegan_meetball_directory, "../images/vegan_meetball.png")

        # Load and display background image
        self.vegan_meetball = CTkImage(dark_image=Image.open(vegan_meetball_directory_path), size=(150, 150))
        self.vegan_meetball = CTkLabel(self.vegan_meetball_frame, image=self.vegan_meetball, text="")
        self.vegan_meetball.grid(row=0, column=0, padx=15)

        # Create labels for name, price, and value
        self.vegan_meetball_name_label = Label(self.vegan_meetball_frame, text="Vegan Me'tBall Wrap", bg="white",
                                             font=("", 9, "bold"))
        self.vegan_meetball_name_label.grid(row=1, column=0, pady=(0, 0))

        self.vegan_meetball_price_label = Label(self.vegan_meetball_frame, text="Price", bg="white", foreground="#9C9C9C")
        self.vegan_meetball_price_label.grid(row=2, column=0, pady=(0, 0))

        self.vegan_meetball_value_label = Label(self.vegan_meetball_frame, text="$ 35.00", bg="white", fg="orange",
                                              font=("", 9, "bold"))
        self.vegan_meetball_value_label.grid(row=3, column=0, pady=(0, 0))

        self.vegan_meetball_add_button = Button(self.vegan_meetball_frame, text="ADD", bg="#F6B100", height=1, width=15,
                                              highlightthickness=0, borderwidth=0, font=("", 8, "bold"))
        self.vegan_meetball_add_button.grid(row=4, column=0, pady=(8, 0), ipady=4)

        vegan_bbq_directory = os.path.dirname(__file__)
        vegan_bbq_directory_path = os.path.join(vegan_bbq_directory, "../images/vegan_bbq.png")

        # Load and display background image
        self.vegan_bbq = CTkImage(dark_image=Image.open(vegan_bbq_directory_path), size=(150, 150))
        self.vegan_bbq = CTkLabel(self.vegan_bbq_frame, image=self.vegan_bbq, text="")
        self.vegan_bbq.grid(row=0, column=0, padx=15)

        # Create labels for name, price, and value
        self.vegan_bbq_name_label = Label(self.vegan_bbq_frame, text="Vegan BBQ Chick'n Panini", bg="white",
                                             font=("", 9, "bold"))
        self.vegan_bbq_name_label.grid(row=1, column=0, pady=(0, 0))

        self.vegan_bbq_price_label = Label(self.vegan_bbq_frame, text="Price", bg="white", foreground="#9C9C9C")
        self.vegan_bbq_price_label.grid(row=2, column=0, pady=(0, 0))

        self.vegan_bbq_value_label = Label(self.vegan_bbq_frame, text="$ 35.00", bg="white", fg="orange",
                                              font=("", 9, "bold"))
        self.vegan_bbq_value_label.grid(row=3, column=0, pady=(0, 0))

        self.vegan_bbq_add_button = Button(self.vegan_bbq_frame, text="ADD", bg="#F6B100", height=1, width=15,
                                              highlightthickness=0, borderwidth=0, font=("", 8, "bold"))
        self.vegan_bbq_add_button.grid(row=4, column=0, pady=(8, 0), ipady=4)

        creamy_mac_directory = os.path.dirname(__file__)
        creamy_mac_directory_path = os.path.join(creamy_mac_directory, "../images/vegan_bbq.png")

        # Load and display background image
        self.creamy_mac = CTkImage(dark_image=Image.open(creamy_mac_directory_path), size=(150, 150))
        self.creamy_mac = CTkLabel(self.creamy_mac_frame, image=self.creamy_mac, text="")
        self.creamy_mac.grid(row=0, column=0, padx=15)

        # Create labels for name, price, and value
        self.creamy_mac_name_label = Label(self.creamy_mac_frame, text="Creamy Mac & Cheese", bg="white",
                                             font=("", 9, "bold"))
        self.creamy_mac_name_label.grid(row=1, column=0, pady=(0, 0))

        self.creamy_mac_price_label = Label(self.creamy_mac_frame, text="Price", bg="white", foreground="#9C9C9C")
        self.creamy_mac_price_label.grid(row=2, column=0, pady=(0, 0))

        self.creamy_mac_value_label = Label(self.creamy_mac_frame, text="$40.00", bg="white", fg="orange",
                                              font=("", 9, "bold"))
        self.creamy_mac_value_label.grid(row=3, column=0, pady=(0, 0))

        self.creamy_mac_add_button = Button(self.creamy_mac_frame, text="ADD", bg="#F6B100", height=1, width=15,
                                              highlightthickness=0, borderwidth=0, font=("", 8, "bold"))
        self.creamy_mac_add_button.grid(row=4, column=0, pady=(8, 0), ipady=4)

# ======================================== History ===========================================================

        self.history_label = Label(self.history_frame, text="H i s t o r y", bg="white", font=("", 10, "bold"))
        self.history_label.grid(row=0, column=0, padx=150)

# ======================================== Check out ===========================================================

        self.checkout_label = Label(self.checkout_frame, text="C h e c k o u t", bg="white", font=("", 10, "bold"))
        self.checkout_label.grid(row=0, column=0, padx=150)
        
        