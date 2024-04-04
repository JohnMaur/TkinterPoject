from models.main import Model
from views.main import View
from .home import HomeController
from .signin import SignInController
from .signup import SignUpController

class Controller:
    def __init__(self, model: Model, view: View):
        self.view = view
        self.model = model
        self.signin_controller = SignInController(model, view)
        self.signup_controller = SignUpController(model, view)
        self.home_controller = HomeController(model, view)

        self.model.auth.add_event_listener(
            "auth_changed", self.auth_state_listener
        )

    def auth_state_listener(self, data):
        if data.is_logged_in:
            self.home_controller.update_view()
            self.home_controller.fetch_and_display_checkout_items()
            self.view.switch("home")
        else:
            self.view.switch("signin")

    def start(self):
        print("Starting...")
        # self.model.auth.load_auth_state()
        if self.model.auth.is_logged_in:
            self.view.switch("home")
        else:
            self.view.switch("signin")

        self.view.start_mainloop()
