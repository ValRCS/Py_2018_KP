import sqlite3


class Database:
    database_file = "pq.db"

    def __init__(self):
        try:
            self._con = sqlite3.connect(self.database_file)
            self._cur = self._con.cursor()

            self._execute(
                "CREATE TABLE IF NOT EXISTS SAVED_SEARCHES "
                "("
                "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                "name TEXT,"
                "tag TEXT,"
                "url TEXT"
                ")"
            )
        except sqlite3.Error as e:
            print(f"Error {e.args[0]}. Failed open a connection to the database.")

    def _execute(self, statement):
        try:
            self._cur.execute(statement)
            self._con.commit()
        except sqlite3.Error as e:
            print(f"Error {e.args[0]}. Failed to execute a statement.")

    def _fetch(self):
        try:
            return self._cur.fetchall()
        except sqlite3.Error as e:
            print(f"Error {e.args[0]}. Failed to fetch results.")
            return None

    def save_search(self, search):
        try:
            name = search["name"]
            tag = search["tag"]
            url = search["url"]
            if name is None or tag is None or url is None:
                return

            self._execute(
                f"INSERT INTO SAVED_SEARCHES VALUES(null, '{name}', '{tag}', '{url}')"
            )
        except sqlite3.Error as e:
            print(f"Error {e.args[0]}. Failed to execute a statement.")

    def get_saved_searches(self):
        try:
            self._execute("SELECT * FROM SAVED_SEARCHES")
            searches = self._fetch()
        except sqlite3.Error as e:
            print(f"Error {e.args[0]}. Failed to execute a statement.")
            searches = None

        return searches

    def close(self):
        if self._con:
            self._con.close()
