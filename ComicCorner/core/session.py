from datetime import datetime
from database.db import Database


class UserSession:
    """
    UserSession is a class that represents a user's session.

    args:
        - username: The username of the user.
        - db: The database to use.

    attributes:
        - username: The username of the user.
        - date: The date of the user's session.
        - db: The database to use.
    """

    def __init__(self, username: str, db: Database):
        self.username = username
        self.date = None
        self.db = db

class Sessions:
    """
    Sessions is a class that represents the collection of active sessions.

    args:
        - None

    attributes:
        - sessions: A dictionary of user sessions.
    """

    def __init__(self):
        self.sessions = {}

    def add_new_session(self, username: str, db: Database) -> None:
        """
        Adds a new user session to the collection of sessions.

        args:
            - username: The username of the user.
            - db: The database to use.

        returns:
            - None
        """
        self.sessions[username] = UserSession(username, db)

    def get_session(self, username: str) -> UserSession:
        """
        Gets a user session from the collection of sessions.

        args:
            - username: The username of the user.

        returns:
            - The user session, or None if it is not found.
        """
        if username in self.sessions: 
          return self.sessions[username]
        return None

    def remove_session(self, username: str) -> None:
        """
        Removes a user session from the collection of sessions.

        args:
            - username: The username of the user.

        returns:
            - None
        """
        del self.sessions[username]

    def get_all_sessions(self) -> dict:
        """
        Gets all user sessions from the collection of sessions.

        args:
            - None

        returns:
            - A dictionary of user sessions.
        """
        return self.sessions
    