from tkinter import messagebox

class SignInController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.frame = self.view.frames["signin"]
        self._bind()

    def _bind(self):
        # Configure the command for the sign-in button
        self.frame.signin_btn.config(command=self.signin)

        # Bind the <Return> key event to the password entry field
        self.frame.signin_btn.focus_set()
        self.frame.signin_btn.bind("<Return>", lambda event: self.signin())

        # Configure the command for the sign-up button
        self.frame.signup_btn.config(command=self.signup)

    def signup(self):
        self.view.switch("signup")

    def signin(self, event=None):
        # Retrieve username and password from the sign-in view
        username = self.frame.username_input.get()
        password = self.frame.password_input.get()

        # Create a dictionary with username and password
        data = {"username": username, "password": password}

        # Pass the data to the authentication model's login method
        login_success = self.model.auth.login(username, password)

        # Check if login was successful
        if login_success:
            # Clear password field
            self.frame.password_input.delete(0, 'end')
            # Redirect to home page or perform other actions
            # Example: self.view.switch("home")
            # Set the user's ID in the model for further use
            self.model.auth.current_user_id = self.model.auth.current_user["userID"]
            # Redirect to the home page
            self.view.switch("home")
        else:
            # Display error message or perform other actions
            messagebox.showerror("Login Error", "Invalid username or password")
