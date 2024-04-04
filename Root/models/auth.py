from .base import ObservableModel

class Auth(ObservableModel):
    def __init__(self):
        super().__init__()
        self.is_logged_in = False
        self.current_user = None

    def login(self, username, password):
        query = "SELECT * FROM user_login WHERE userName = %s AND userPass = %s"
        params = (username, password)
        result = self.execute_query(query, params)
        if result:
            # Fetch the first row (assuming there's only one user with the provided credentials)
            user_data = result[0]
            # Store the user data in the current_user attribute
            self.current_user = {"userID": user_data[0], "username": user_data[1], "password": user_data[2]}  # Include userID
            self.is_logged_in = True
            self.trigger_event("auth_changed")
            return True
        else:
            return False

    def logout(self):
        self.is_logged_in = False
        self.current_user = None
        self.trigger_event("auth_changed")

    def add_to_checkout(self, item_name, item_price, user_id):
        cursor = self._db_connection.cursor()
        try:
            query = "INSERT INTO checkout (product_name, product_price, user_id) VALUES (%s, %s, %s)"
            cursor.execute(query, (item_name, item_price, user_id))
            self._db_connection.commit()
        except Exception as e:
            print("Error adding to checkout:", e)
            self._db_connection.rollback()
        finally:
            cursor.close()

    def remove_from_checkout(self, item_name, item_price, user_id):
        cursor = self._db_connection.cursor()
        try:
            query = "DELETE FROM checkout WHERE product_name = %s AND product_price = %s AND user_id = %s"
            cursor.execute(query, (item_name, item_price, user_id))
            self._db_connection.commit()
        except Exception as e:
            print("Error removing from checkout:", e)
            self._db_connection.rollback()
        finally:
            cursor.close()

    def add_to_history(self, item_name, item_price, user_id):
        cursor = self._db_connection.cursor()
        try:
            query = "INSERT INTO history (product_name, product_price, user_id) VALUES (%s, %s, %s)"
            cursor.execute(query, (item_name, item_price, user_id))
            self._db_connection.commit()
        except Exception as e:
            print("Error adding to history:", e)
            self._db_connection.rollback()
        finally:
            cursor.close()

    def fetch_checkout_items(self, user_id):
        cursor = self._db_connection.cursor()
        try:
            query = "SELECT product_name, product_price FROM checkout WHERE user_id = %s"
            cursor.execute(query, (user_id,))
            return cursor.fetchall()  # Returns a list of tuples (item_name, item_price)
        except Exception as e:
            print("Error fetching checkout items:", e)
        finally:
            cursor.close()



