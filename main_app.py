from flask import Flask
from flask import render_template
from flask import abort, redirect, url_for 

app = Flask(__name__)

@app.route("/")
def main():
    return redirect(url_for('index'))

@app.route("/profile")
def index():
    return render_template('index.html')