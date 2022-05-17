from flask import Flask, render_template, session

app = Flask(__name__)

@app.route('/')
def index():
    if session['name']:
        return render_template('home.html')

    return render_template('index.html')

@app.route('/login' method=['GET', 'POST'])
def login():
    return render_template('login.html')