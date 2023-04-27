import sqlite3
import uuid


def dict_factory(cursor: sqlite3.Cursor, row: tuple) -> dict:
    """
    Creates a dictionary from a row in the database. This is used to convert the rows into dictionaries.

    args:
        - cursor: The cursor of the database, which is a built-in sqlite3 class.
        - row: The row to convert into a dictionary.

    returns:
        - The dictionary of the row.
    """

    row_dict = {}
    for index, column in enumerate(cursor.description):
        row_dict[column[0]] = row[index]
    return row_dict


def generate_unique_id() -> str:
    """
    Generates a unique ID.

    args:
        - None

    returns:
        - A unique ID as a string.
    """
    return str(uuid.uuid4())
