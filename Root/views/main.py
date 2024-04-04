from .root import Root
from .home import HomeView
from .signin import SignInView
from .signup import SignUpView

class View:
    def __init__(self):
        self.root = Root()
        self.frames = {}

        self._add_frame(SignUpView, "signup", width=850, height=500, x=250, y=100)
        self._add_frame(SignInView, "signin")
        self._add_frame(HomeView, "home")

    def _add_frame(self, Frame, name, width=None, height=None, x=None, y=None):
        self.frames[name] = Frame(self.root)
        if width and height:
            self.frames[name].config(width=width, height=height)
        if x and y:
            self.root.geometry(f"{width}x{height}+{x}+{y}")
        self.frames[name].grid(row=0, column=0, sticky="nsew")

    def switch(self, name):
        frame = self.frames[name]
        frame.tkraise()

    def start_mainloop(self):
        self.root.mainloop()