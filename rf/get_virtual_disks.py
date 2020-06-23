def get_virtual_disks(rfo, api=1, unit=1):
    """ Get virtual disks

    Parameters:
    rfo (object): Redfish Client Login Object
    api (int): API Value
    unit (int): Unit Value

    Returns:
    array of dict: virtual disks
    """
    res = rfo.get(f"/redfish/v{api}/Systems/{unit}")
    url = res.dict['Oem']['Hpe']['SmartStorageConfig'][0]['@odata.id']
    res = rfo.get(url)
    if res.status != 200:
        print(f"Error: {res.status}: {res.read}")
        return "XXX"
    return res.dict['LogicalDrives']

