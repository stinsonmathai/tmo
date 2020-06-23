def get_license_key(rfo, api=1, unit=1):
    """Obtain server license key

    Parameters:
    rfo (object): Redfish Client Login Object
    api (int): API Value
    unit (int): Unit Value

    Returns:
    str: license key
    """
    res = rfo.get(f"/redfish/v{api}/Managers/{unit}/")
    if res.status != 200:
        print(f"Error: {res.status}: {res.read}")
        return "XXX"
    return str(res.dict['Oem']['Hpe']['License']['LicenseKey']) + str(res.dict['Oem']['Hpe']['License']['LicenseString'])

