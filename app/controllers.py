from app import app

from catalog.catalog_transformer import transform_catalog
from gbp.gbp_transformer import transform_gbp

from flask import render_template, request

@app.route('/')
def index():
    return render_template("index.html", has_results=False)

@app.route('/', methods=['POST'])
def search():
    catalog_cc = transform_catalog(request.form["ccNumber"])
    gbp_info = transform_gbp(catalog_cc)

    return render_template("index.html", 
        has_results=True, 
        catalog_cc = catalog_cc,
        gbp_info = gbp_info)