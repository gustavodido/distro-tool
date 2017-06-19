from requests import get
from json import loads

catalog_url = "http://allocation-catalog-service.apps.cfprod.phx.gaptech.com"

def get_cc(ccNumber):
    url = catalog_url + "/allocation/in-season/allocated-customer-choices/search?level=CC&code="
    return loads(get(url + ccNumber).text)[0]

def get_cc_resource(ccId):
    return catalog_url + "/allocation/in-season/allocated-customer-choices/" + ccId
