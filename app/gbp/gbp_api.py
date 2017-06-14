from requests import get
from json import loads

def get_distro_information(distroId):
    url = "http://gbp-production.phx.gapinc.com/store-service/planning/store-plan/assortment-strategies/"
    return loads(get(url + distroId).text)["resource"]