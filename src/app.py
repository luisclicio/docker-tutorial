from flask import Flask, request, redirect, url_for, render_template

from data import Database


db = Database()
app = Flask(__name__)

@app.get('/')
def index():
    users = db.get_all_users()
    return render_template('index.html', users=users)

@app.post('/api/users')
def add_user():
    db.add_user({
        'name': request.form['name'],
        'email': request.form['email'],
        'password': request.form['password'],
    })
    return redirect(url_for('index'))

@app.get('/api/users')
def get_all_users():
    return db.get_all_users()
