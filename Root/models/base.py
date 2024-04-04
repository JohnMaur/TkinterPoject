import mysql.connector

class ObservableModel:
    def __init__(self):
        self._event_listeners = {}
        self._db_connection = None

    def connect_to_database(self, host, username, password, database):
        self._db_connection = mysql.connector.connect(
            host=host,
            user=username,
            password=password,
            database=database
        )

    def execute_query(self, query, params=None, commit=False):
        cursor = self._db_connection.cursor()
        try:
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            if commit:
                self._db_connection.commit()  # Commit the transaction if commit is True
            result = cursor.fetchall()
            return result
        except Exception as e:
            print("Error executing query:", e)
            self._db_connection.rollback()  # Rollback the transaction if an error occurs
        finally:
            cursor.close()

    def add_event_listener(self, event, fn):
        try:
            self._event_listeners[event].append(fn)
        except KeyError:
            self._event_listeners[event] = [fn]

        return lambda: self._event_listeners[event].remove(fn)

    def trigger_event(self, event):
        if event not in self._event_listeners.keys():
            return

        for func in self._event_listeners[event]:
            func(self)
