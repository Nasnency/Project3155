#!/usr/bin/env python3

from authentication.authTools import login_pipeline, update_passwords, hash_password
from database.db import Database
from flask import Flask, render_template, request, redirect, url_for, abort
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
session_current = None
#sessions.add_new_session(username, db)


@app.route('/')
def index_page():
    """
    permanent redirect to home page
    """
    return redirect(url_for('home'))


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
    global username, session_current
    sessions.remove_session(username)
    username = None
    session_current = None
    return redirect(url_for('home'))

@app.route('/home')
def home():
  comictodisplay = latest_comic
  comments=None
  page_id=None
  if request.args.get('page'):
    print("got a page: " + request.args.get('page'))
    resp=db.get_indexed_comic(request.args.get('page'))
    if(resp['rowid']):
      comictodisplay=resp
      page_id=resp['rowid']
    else:
      abort(404)
  else:
    print("no page given, defaulting to latest")
    page_id=latest_comic['rowid']
      
  comments=db.get_comments(page_id)
  return render_template('index.html', comic=comictodisplay, latest=latest_comic, comments=comments, curr_session=session_current)

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
        global username, sessions, session_current
        username = uname
        sessions.add_new_session(uname, db)
        session_current = sessions.get_session(uname)
        print("uname: " + session_current.username)
        return redirect(url_for('home'))
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
      return redirect(url_for('home'))
    else:
      return render_template('register.html', message="username taken already!")

@app.route('/comment', methods=['POST'])
def post_comment():

  content = request.form['comment-input']
  comic_id = request.form['page-id']
  username = request.form['username']

  db.insert_comment(username, content, comic_id)

  return redirect(url_for('home') + "?page=" + request.form['page-id'])

@app.route('/DEBUG_throw_404')
def throw_404():
  abort(404)

@app.route('/DEBUG_throw_500')
def throw_500():
  abort(500)

@app.errorhandler(404)
def page_not_found(e):
  return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(e):
  return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True, host=HOST, port=PORT)
