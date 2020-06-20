from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World"

@app.route("/contato")
def contato():
    return  "<form><input type='text'>        "

