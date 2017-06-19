from gbp_api import get_distro_information, get_distro_information_resource, get_rolling_distro

def transform_gbp(cc):
    return {
     "distros_information": transform_distro_information(cc),
     "rolling_distro_stores": transform_rolling_distro(cc)
    }

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

