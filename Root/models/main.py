from .auth import Auth

class Model:
    def __init__(self):
        self.auth = Auth()
        self.auth.connect_to_database(host="localhost", username="root", password="root123", database="point_of_sale")