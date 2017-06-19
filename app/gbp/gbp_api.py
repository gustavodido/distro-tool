from requests import get,post
from json import loads

gbp_url = "http://gbp-production.phx.gapinc.com"

def get_distro_information_resource(distroId):
  return gbp_url + "/store-service/planning/store-plan/assortment-strategies/" + distroId

def get_distro_information(distroId):
    return loads(get(get_distro_information_resource(distroId)).text)["resource"]

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