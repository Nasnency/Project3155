#!/usr/bin/env python3

from authentication.authTools import login_pipeline, update_passwords, hash_password
from database.db import Database
from flask import Flask, render_template, request
from core.session import Sessions

app = Flask(__name__)
HOST, PORT = 'localhost', 8080
global username, products, db, sessions
username = 'default'
db = Database('database/comicData.db')
#products = db.get_full_inventory()
comics = db.get_comics()
latest_comic = db.get_latest_comic()
sessions = Sessions()
#sessions.add_new_session(username, db)


@app.route('/')
def index_page():
    """
    Renders the index page when the user is at the `/` endpoint, passing along default flask variables.

    args:
        - None

    returns:
        - None
    """
    return render_template('index.html', username=username, latest=latest_comic, sessions=sessions)


@app.route('/login')
def login_page():
    """
    Renders the login page when the user is at the `/login` endpoint.

    args:
        - None

    returns:
        - None
    """
    return render_template('login.html')

@app.route('/logout', methods=['POST'])
def logout():
    """
    Returns the user to the home index and ends their session when the user is at the /logout endpoint with a POST request.

    args:
        - None

    returns:
        - None

    modifies:
        - sessions: terminates the session
    """
    global username
    sessions.remove_session(username)
    username = None
    return render_template('index.html', username=username, latest=latest_comic, sessions=sessions)


@app.route('/home', methods=['POST'])
def login():
    """
    Renders the home page when the user is at the `/home` endpoint with a POST request.

    args:
        - None

    returns:
        - None

    modifies:
        - sessions: adds a new session to the sessions object

    """
    uname = request.form['username']
    pword = request.form['password']
    if login_pipeline(uname, pword, db):
        global username, sessions
        username = uname
        sessions.add_new_session(uname, db)
        return render_template('index.html', username=uname, latest=latest_comic, sessions=sessions)
    else:
        return render_template('login.html')


@app.route('/register')
def register_page():
    """
    Renders the register page when the user is at the `/register` endpoint.

    args:
        - None

    returns:
        - None
    """
    return render_template('register.html')


@app.route('/register', methods=['POST'])
def register():
    """
    Renders the index page when the user is at the `/register` endpoint with a POST request.

    args:
        - None

    returns:
        - None

    modifies:
        - passwords.txt: adds a new username and password combination to the file
        - database/storeRecords.db: adds a new user to the database
    """
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    salt, key = hash_password(password)
    update_passwords(username, key, salt)
    #forces them to be a reader
    if db.insert_user(username, key, email, first_name, last_name, salt, 0) == 0:
      return render_template('index.html', username=username, latest=latest_comic, sessions=sessions)
    else:
      return render_template('register.html', message="username taken already!")

"""
#no longer used
@app.route('/checkout', methods=['POST'])
def checkout():
   
    Renders the checkout page when the user is at the `/checkout` endpoint with a POST request.

    args:
        - None

    returns:
        - None

    modifies:
        - sessions: adds items to the user's cart
    
    order = {}
    user_session = sessions.get_session(username)
    for item in products:
        print(f"item ID: {item['id']}")
        if request.form[str(item['id'])] > '0':
            count = request.form[str(item['id'])]
            order[item['item_name']] = count
            user_session.add_new_item(
                item['id'], item['item_name'], item['price'], count)

    user_session.submit_cart()

    return render_template('checkout.html', order=order, sessions=sessions, total_cost=user_session.total_cost)
"""

if __name__ == '__main__':
    app.run(debug=True, host=HOST, port=PORT)
