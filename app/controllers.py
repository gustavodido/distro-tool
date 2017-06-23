from app import app

from catalog.catalog_transformer import transform_catalog
from gbp.gbp_transformer import transform_gbp

from catalog.catalog_api import refresh_distro_name, refresh_dc_mapping, refresh_distro_stores

from flask import render_template, request, jsonify

@app.route('/', defaults={'cc': None})
@app.route('/<int:cc>')
def index(cc):
    if not cc:
        return render_template("index.html", has_results=False)

    return do_search(str(cc))

@app.route('/', methods=['POST'])
def search():
    return do_search(request.form["ccNumber"])

@app.route('/api/refresh-distro-name', methods=['GET'])
def refresh_distro_name_action():
    return jsonify(refresh_distro_name(request.args.get("ccNumber")))

@app.route('/api/refresh-distro-stores', methods=['GET'])
def refresh_distro_stores_action():
    return jsonify(refresh_distro_stores(request.args.get("ccNumber")))

@app.route('/api/refresh-dc-mapping', methods=['GET'])
def refresh_dc_mapping_action():
    return jsonify(refresh_dc_mapping(request.args.get("ccNumber")))

def do_search(cc):
    catalog_cc = transform_catalog(cc)
    gbp_info = transform_gbp(catalog_cc)

    return render_template("index.html", 
        has_results=True, 
        catalog_cc = catalog_cc,
        gbp_info = gbp_info)
