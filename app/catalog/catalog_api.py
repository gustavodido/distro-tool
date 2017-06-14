from requests import get
from json import loads

def get_cc(ccNumber):
    url = "http://allocation-catalog-service.apps.cfprod.phx.gaptech.com/allocation/in-season/allocated-customer-choices/search?level=CC&code="
    return loads(get(url + ccNumber).text)[0]