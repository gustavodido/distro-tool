from requests import get,post
from json import loads

def get_distro_information(distroId):
    url = "http://gbp-production.phx.gapinc.com/store-service/planning/store-plan/assortment-strategies/"
    return loads(get(url + distroId).text)["resource"]

def get_rolling_distro(distroId, subClass, startDate, endDate):
    url = "http://gbp-production.phx.gapinc.com/store-service/planning/in-season-store-plan/rolling-distro-store-lists/search"
    payload = {
          "rollingDistroStoreListRequest": {
            "merchandiseHierarchyNode": subClass,
            "timeBasedAssortmentStrategies": [
              {
                "startDate": startDate, 
                "endDate": endDate,
                "assortmentStrategyId": distroId
              }
            ]
          }
        }

    result = post(url , json=payload).text
    return loads(result)["resource"]    