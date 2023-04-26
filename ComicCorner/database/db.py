from core.utils import dict_factory, calculate_cost
import datetime as dt
import sqlite3


class Database:
    """
    A class that handles all database operations.

    args:
        - database_path: The path to the database file.

    attributes:
        - database_path: The path to the database file.
        - connection: The connection to the database.
        - cursor: The cursor of the database.
    """

    def __init__(self, database_path: str = "storeRecords.db") -> None:
        self.database_path = database_path
        self.connection = sqlite3.connect(
            database_path, check_same_thread=False)
        self.connection.row_factory = dict_factory
        self.cursor = self.connection.cursor()

    # --------------------------------------------
    # ----------------- Comics -------------------
    # --------------------------------------------

    def get_comics(self):
        self.cursor.execute("SELECT * FROM comic")
        return self.cursor.fetchall()

    def get_latest_comic(self):
        self.cursor.execute("SELECT page_name, image_url, MAX(rowid) as rowid FROM comic")
        return self.cursor.fetchone()

    def get_indexed_comic(self, index: str):
        self.cursor.execute("SELECT page_name, image_url, MAX(rowid) as rowid FROM comic WHERE rowid=" + index)
        return self.cursor.fetchone()
    
    # --------------------------------------------
    # ---------------- Comments ------------------
    # --------------------------------------------

    def get_comments(self, index: int):
      self.cursor.execute("SELECT username, content, comic_id, rowid as comment_id FROM comment WHERE comic_id=" + str(index))
      return self.cursor.fetchall()

    def insert_comment(self, username: str, content: str, comic_id: int):
      self.cursor.execute("INSERT INTO comment (username, content, comic_id) VALUES (?, ?, ?)", (username, content, comic_id))
      self.connection.commit()

    # --------------------------------------------
    # ------------------ Users -------------------
    # --------------------------------------------

    def get_login_data(self):
        self.cursor.execute("SELECT `username`, `password_salt`, `password_hash` FROM users")
        return self.cursor.fetchall()

    def insert_user(self, username: str, password_hash: str, email: str, first_name: str, last_name: str, password_salt: str, session_type: str) -> int:
        """
        Inserts a new user into the database.

        args:
            - username: The username of the user to insert.
            - password_hash: The password_hash of the user to insert.
            - email: The email of the user to insert.

        returns:
            - None
        """
        try:
          self.cursor.execute(
              "INSERT INTO users (username, password_hash, password_salt, email, first_name, last_name, session_type) VALUES (?, ?, ?, ?, ?, ?, ?)",
              (username, password_hash, password_salt, email, first_name, last_name, session_type))
          self.connection.commit()
          return 0
        except sqlite3.IntegrityError as e:
          #username wasn't unique
          return 1



    # ------ Getter methods ------

    def get_all_user_information(self):
        """
        Gets all user information from the database.

        args:
            - None

        returns:
            - A list of all user information in the database.
        """
        self.cursor.execute("SELECT * FROM users")
        return self.cursor.fetchall()

    def get_password_hash_by_username(self, username: str):
        """
        Gets the password hash of a user from the database.

        args:
            - username: The username of the user whose password hash to get.

        returns:
            - The password hash for the user with the given username.
        """
        self.cursor.execute(
            "SELECT password_hash FROM users WHERE username = ?", (username,))
        return self.cursor.fetchone()

    def get_email_by_username(self, username: str):
        """
        Gets the email of a user from the database.

        args:
            - username: The username of the user whose email to get.

        returns:
            - The email for the user with the given username.
        """
        self.cursor.execute(
            "SELECT email FROM users WHERE username = ?", (username,))
        return self.cursor.fetchone()

    def get_first_name_by_username(self, username: str):
        """
        Gets the first name of a user from the database.

        args:
            - username: The username of the user whose first name to get.

        returns:
            - The first name for the user with the given username.
        """
        self.cursor.execute(
            "SELECT first_name FROM users WHERE username = ?", (username,))
        return self.cursor.fetchone()

    def get_last_name_by_username(self, username: str):
        """
        Gets the last name of a user from the database.

        args:
            - username: The username of the user whose last name to get.

        returns:
            - The last name for the user with the given username.
        """
        self.cursor.execute(
            "SELECT last_name FROM users WHERE username = ?", (username,))
        return self.cursor.fetchone()

    # ------ Setter methods ------

    def set_password_hash(self, username: str, new_password_hash: str):
        """
        Updates the password hash of a user in the database.

        args:
            - username: The username of the user to update.
            - new_password_hash: The new password hash of the user.

        returns:
            - None
        """
        self.cursor.execute(
            "UPDATE users SET password_hash = ? WHERE username = ?", (new_password_hash, username))
        self.connection.commit()

    def set_email(self, username: str, new_email: str):
        """
        Updates the email of a user in the database.

        args:
            - username: The username of the user to update.
            - new_email: The new email of the user.

        returns:
            - None
        """
        self.cursor.execute(
            "UPDATE users SET email = ? WHERE username = ?", (new_email, username))
        self.connection.commit()

    def set_first_name(self, username: str, new_first_name: str):
        """
        Updates the first name of a user in the database.

        args:
            - username: The username of the user to update.
            - new_first_name: The new first name of the user.

        returns:
            - None
        """
        self.cursor.execute(
            "UPDATE users SET first_name = ? WHERE username = ?", (new_first_name, username))
        self.connection.commit()

    def set_last_name(self, username: str, new_last_name: str):
        """
        Updates the last name of a user in the database.

        args:
            - username: The username of the user to update.
            - new_last_name: The new last name of the user.

        returns:
            - None
        """
        self.cursor.execute(
            "UPDATE users SET last_name = ? WHERE username = ?", (new_last_name, username))
        self.connection.commit()

