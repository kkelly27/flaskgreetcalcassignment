from flask import Flask

app = Flask(kelly)

@app.route('/welcome')
def welcome():
    return "welcome"

@app.route('welcome/back')
def welcome():
    return "welcome back"

@app.route('/welcome/home')
def welcome_home():
    return "welcome home"