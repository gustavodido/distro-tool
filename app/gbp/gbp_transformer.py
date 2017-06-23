from gbp_api import get_store_list, get_distro_information, get_distro_information_resource, get_rolling_distro

def transform_gbp(cc):
    result = {
     "distros_information": transform_distro_information(cc),
     "rolling_distro_stores": transform_rolling_distro(cc),
    }

    storeListId = get(cc, "storeListId")
    result["hasStoreListId"] = False
    if storeListId:
        strategies = get_store_list(cc["storeListId"]) 
        result["ccStoreList"] = addStoreComparision(cc, strategies)
        result["hasStoreListId"] = True

    return result

def transform_distro_information(cc):
    distros_information = []
    for distro in cc["distros"]:
        distro_info = get_distro_information(distro["id"]);
        distro_info["resource"] = get_distro_information_resource(distro["id"])
        distros_information.append(distro_info)

    return distros_information 

def transform_rolling_distro(cc):
    distros = []
    for distro in cc["distros"]:
        startDate = distro["inStoreStartDate"]
        endDate = distro["markdownDate"]
        rolling_distro = get_rolling_distro(distro["id"], cc["subClassId"], startDate, endDate)
        distro["rollingDistro"] = rolling_distro
            
        distros.append(distro)
        
    return distros

def addStoreComparision (cc, strategies):
    locations = set()
    for distro in cc["distros"]:
        for location in distro["activeStores"]:
            locations.add(location["storeNumber"])


    for strategy in strategies["timeBasedStores"]:
        gbp_locations = set()
        for location in strategy["storeList"]:
            if location["location"]["status"] == "ACTIVE":
                gbp_locations.add(location["locationNumber"])

            strategy["missing_catalog"] = gbp_locations - locations
            strategy["missing_gbp"] = locations - gbp_locations
            strategy["activeStoreCount"] = len(gbp_locations)
            strategy["has_differences"] = len(strategy["missing_catalog"]) == 0 and len(strategy["missing_gbp"]) == 0

    return strategies

def get(cc, field):
    if field in cc:
        return cc[field]
    return None

