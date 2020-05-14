def get_disk_blob(rfo, api=1, unit=1):
    """Aggregate disk information

    Parameters:
    rfo (object): Redfish Client Login Object
    api (int): API Value
    unit (int): Unit Value

    Returns:
    list: JSON
    """
    blob = []
    res = rfo.get(f"/redfish/v{api}/Chassis/{unit}")
    if res.status != 200:
        print(f"Error: {res.status}: {res.read}")
        return "XXX"
    members = res.dict['Links']['Drives']
    for m in members:
        res = rfo.get(m['@odata.id'])
        if res.status != 200:
            print(f"Member Error: {res.status}: {res.read}")
            return "XXX"
        blob.append(res.dict)
    return blob

