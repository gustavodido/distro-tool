from app import app

from flask import render_template

@app.route('/')
def index():
    return render_template("index.html", has_results=False)

@app.route('/', methods=['POST'])
def search():
    return render_template("index.html", has_results=True)