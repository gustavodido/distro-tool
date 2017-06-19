from app import app

from catalog.catalog_transformer import transform_catalog
from gbp.gbp_transformer import transform_gbp

from flask import render_template, request

@app.route('/', defaults={'cc': None})
@app.route('/<path:cc>')
def index(cc):
    if not cc:
        return render_template("index.html", has_results=False)

    return do_search(cc)

@app.route('/', methods=['POST'])
def search():
    return do_search(request.form["ccNumber"])

def do_search(cc):
    catalog_cc = transform_catalog(cc)
    gbp_info = transform_gbp(catalog_cc)

    return render_template("index.html", 
        has_results=True, 
        catalog_cc = catalog_cc,
        gbp_info = gbp_info)
