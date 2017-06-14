from gbp_api import get_distro_information

def transform_gbp(cc):
    distros_information = []
    for distro in cc["distros"]:
        distros_information.append(get_distro_information(distro["id"]))

    return {
     "distros_information": distros_information
    }