from hashlib import sha512
import os

#this is to get the database in
import sys
sys.path.append("..")
from database.db import Database


def hash_password(password: str, salt: str = None) -> tuple:
    """
    Hashes a password using SHA-512.

    args:
        - password: A string of the password to hash.

    returns:
        - A tuple of the salt and the hashed password, both as strings.
    """
    encoded_password = password.encode()
    if salt is None:
        salt = os.urandom(16).hex()
    key = sha512(encoded_password + salt.encode()).hexdigest()
    return (salt, key)


def username_exists(username: str, db: Database) -> bool:
    """
    Checks if a username exists in the passwords.txt file.

    args:
        - username: A string of the username to check.

    returns:
        - True if the username exists, False if not.
    """

    """
    #no longer used
    with open("authentication/passwords.txt", "r") as file:
        lines = file.readlines()
    for line in lines:
        if line.split(":")[0] == username:
            return True
    return False
    """
    accts = db.get_login_data()
    for acct in accts:
        if acct['username'] == username:
            return True
    return False


def check_password(password: str, salt: str, key: str) -> bool:
    """
    Checks if a password is correct by hashing it and comparing it to the given hash key.

    args:
        - password: A string of the password to check.
        - salt: A string of the salt to use.
        - key: A string of the hash to check against.

    returns:
        - True if the password is correct, False if not.
    """
    salt, new_key = hash_password(password, salt)
    key, new_key = key.strip(), new_key.strip()

    return key == new_key


def login_pipeline(username: str, password: str, db: Database) -> bool:
    """
    Checks if a username and password combination is correct.

    args:
        - username: A string of the username to check.
        - password: A string of the password to check.

    returns:
        - True if the username and password combination is correct, False if not.
    """
    if not username_exists(username, db):
        return False

    accts = db.get_login_data()
    for acct in accts:
        if acct['username'] == username:
            return check_password(password, acct['password_salt'], acct['password_hash'])
    return False

def main():
    password = input("enter password: ")
    salt, key = hash_password(password)
    print(f"Salt: {salt}")
    print(f"Key: {key}")


if __name__ == "__main__":
    main()
