from app import app

from catalog_api import get_cc
from catalog_transformer import transform_catalog

from flask import render_template, request

@app.route('/')
def index():
    return render_template("index.html", has_results=False)

@app.route('/', methods=['POST'])
def search():
    catalog_cc = transform_catalog(get_cc(request.form["ccNumber"]))
    return render_template("index.html", 
        has_results=True, 
        catalog_cc = catalog_cc)