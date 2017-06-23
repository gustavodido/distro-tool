from requests import get, post
from json import loads

catalog_url = "http://allocation-catalog-service.apps.cfprod.phx.gaptech.com"

def get_cc(ccNumber):
    url = catalog_url + "/allocation/in-season/allocated-customer-choices/search?level=CC&code="
    return loads(get(url + ccNumber).text)[0]

def get_cc_resource(ccId):
    return catalog_url + "/allocation/in-season/allocated-customer-choices/" + ccId

def refresh_distro_name(ccNumber):
    status_code = 404

    if not ccNumber is None and not ccNumber == "":
        url = catalog_url + "/allocation/distro/update-info"
        result = post(url , json=get_query_payload(ccNumber))
        status_code = result.status_code 

    return { "result": status_code }

def refresh_distro_stores(ccNumber):
    status_code = 404

    if not ccNumber is None and not ccNumber == "":
        url = catalog_url + "/allocation/api/update-distros"
        result = post(url , json=get_query_payload(ccNumber))
        status_code = result.status_code 

    return { "result": status_code }

def refresh_dc_mapping(ccNumber):
    status_code = 404

    if not ccNumber is None and not ccNumber == "":
        url = catalog_url + "/allocation/api/update-locations"
        result = post(url , json=get_query_payload(ccNumber))
        status_code = result.status_code 

    return { "result": status_code }

def get_query_payload(ccNumber):
    return {
               "level": "CC",
               "code": ccNumber
            }
