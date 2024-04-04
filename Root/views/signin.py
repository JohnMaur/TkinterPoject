from tkinter import Frame, Label, Entry, Button, messagebox
from PIL import Image, ImageTk
from customtkinter import CTkLabel, CTkButton, CTkEntry, CTkImage
import os

class SignInView(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)

        # Create nav frame
        self.left_frame = Frame(self, bg="#DDDDDD")
        self.left_frame.place(x=0, y=0, relheight=1, width=500)

        # Create content frame
        self.right_frame = Frame(self, bg="#EEEEEE")
        self.right_frame.place(x=500, rely=0.22, relheight=1, relwidth=1)

        # Get the absolute path to the image file
        current_directory = os.path.dirname(__file__)
        image_path = os.path.join(current_directory, "../images/bg1.jpg")

        # Load and display background image
        self.bg_img = CTkImage(dark_image=Image.open(image_path), size=(500, 500))
        self.bg_lab = CTkLabel(self.left_frame, image=self.bg_img, text="")
        self.bg_lab.grid(row=0, column=0, columnspan=2, sticky="nsew")

        # Username label and entry
        self.username_label = Label(self.right_frame, text="Username", font=("", 16, "bold"))
        self.username_label.grid(row=0, column=0, sticky="w", padx=50, pady=5)
        self.username_input = Entry(self.right_frame, text="", font=("", 16))
        self.username_input.grid(row=1, column=0, sticky="nwe", padx=50)

        # Password label and entry
        self.password_label = Label(self.right_frame, text="Password", font=("", 16, "bold"))
        self.password_label.grid(row=2, column=0, sticky="w", padx=50, pady=5)
        self.password_input = Entry(self.right_frame, text="", font=("", 16), show="*")
        self.password_input.grid(row=3, column=0, sticky="nwe", padx=50)

        # Login button
        self.signin_btn = Button(self.right_frame, text="Login", font=("", 15), height=1, width=10)
        self.signin_btn.grid(row=4, column=0, sticky="news", pady=30, padx=50)

        # Sign Up button
        self.signup_btn = Button(self.right_frame, text="Sign Up", font=("", 15), height=1, width=15)
        self.signup_btn.grid(row=6, column=0, sticky="nwes", padx=50)

        self.signup_option_label = Label(self.right_frame, text="Don't have an account?", font=("", 12))
        self.signup_option_label.grid(row=5, column=0, sticky="w", padx=50)

