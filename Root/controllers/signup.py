# controllers/signup.py
from tkinter import messagebox

class SignUpController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.frame = self.view.frames["signup"]
        self._bind()

    def _bind(self):
        self.frame.signup_btn.config(command=self.signup)
        self.frame.signin_btn.config(command=self.signin)

    def signin(self):
        self.view.switch("signin")

    def signup(self):
        # Retrieve data from the sign-up view
        username = self.frame.username_input.get()
        password = self.frame.password_input.get()
        confirm_password = self.frame.confirm_password_input.get()
        has_agreed = self.frame.has_agreed.get()

        # Perform basic validation
        if not username or not password or not confirm_password:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match.")
            return

        if not has_agreed:
            messagebox.showerror("Error", "Please agree to the Terms & Conditions.")
            return

        # Insert user data into the database
        query = "INSERT INTO user_login (userName, userPass) VALUES (%s, %s)"
        params = (username, password)

        try:
            self.model.auth.execute_query(query, params, commit=True)
            self.view.switch("signin")
            messagebox.showinfo("Success", "User signed up successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
