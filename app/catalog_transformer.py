
def transform_catalog(cc):
    return {
        "storeListId": get(cc, "storeListId"),
        "skuLocations": len(cc["skus"][0]["locations"]), 
        "subClassId": cc["merchandiseHierarchy"][0]["id"],
        "distros": transform_distros(cc)
    }

def get(cc, field):
    if field in cc:
        return cc[field]
    return None

def transform_distros(cc):
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
            "id": distro["id"],
            "distroName": distro["distroName"],
            "inStoreStartDate": distro["inStoreStartDate"],
            "markdownDate": distro["markdownDate"],
            "activeStores": loc_act,
            "inactiveStores": loc_inac
        })

    return distros