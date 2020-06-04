import json


def get_nic_blob(rfo, api=1, unit=1):
    """This function fetches information about EACH of the network interfaces of the server.

    Parameters:
    object: Redfish Client Login Object
    int: API Value
    int: Unit Value

    Returns:
    list: JSON - Details of each of the Ethernet Interfaces in the Server
    """

    blob = []

    # iLO version
    res = rfo.get(f"/redfish/v{api}/managers/{unit}")
    if "iLO 4" in res.dict['FirmwareVersion']:
        url = f"/redfish/v{api}/systems/{unit}/NetworkAdapters"
    else:
        url = f"/redfish/v{api}/systems/{unit}/EthernetInterfaces"

    res = rfo.get(url)
    if res.status != 200:
        print(f"Error: {res.status}: {res.read}")
        return "XXX"
    members = res.dict['Members']
    for m in members:
        res = rfo.get(m['@odata.id'])
        if res.status != 200:
            print(f"Member Error: {res.status}: {res.read}")
            return "XXX"
        blob.append(res.dict)
    return json.dumps(blob)


