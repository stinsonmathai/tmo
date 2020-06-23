def get_boot_order(rfo, api=1, unit=1):
    """Obtain server boot device order

    Parameters:
    rfo (object): Redfish login session
    api (int): API version
    unit (int): Enumerated component unit

    Returns:
    str: Boot order
    """

    url = f"/redfish/v{api}/systems/{unit}/bios"
    res = rfo.get(url)
    if res.status != 200:
        print(f"Error: {res.status}: {res.read}")
        return "XXX"
    booturl = res.dict['Oem']['Hpe']['Links']['Boot']['@odata.id']
    res = rfo.get(booturl)
    if res.status != 200:
        print(f"HTTP Fail Status: {res.status} - {res.read}")
        return "XXX"
    return res.dict['DefaultBootOrder']

