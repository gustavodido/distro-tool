from app import app
from catalog_api import get_cc

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

def transform_catalog(cc):
    distros = []
    for distro in cc["distros"]:
        loc_inac = []
        loc_act = []
        for dc in distro["distributionCenters"]:
            for location in dc["locations"]:
                if location["active"]:
                    loc_act.append(location)
                else:
                    loc_inac.append(location)

        distros.append({
            "distroName": distro["distroName"],
            "inStoreStartDate": distro["inStoreStartDate"],
            "markdownDate": distro["markdownDate"],
            "activeStores": loc_act,
            "inactiveStores": loc_inac
        })

    return { "distros": distros }