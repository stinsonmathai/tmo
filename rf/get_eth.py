

def get_eth(rfo, api=1, unit=1, nic_name =""):
    """This function fetches the information of a specific NIC on the server.
    URL is https://IP_ADDRESS/redfish/v1/systems/1/
    MODEL information is at the top level of the JSON Hierarchy

    Parameters:
    rfo (object): Redfish Client Login Object
    api (int): API Value
    unit (int): Unit Value

    Returns:
    list: names of the NICS on the server
    """
    res = rfo.get(f"/redfish/v{api}/Systems/{unit}/EthernetInterfaces")
    if res.status != 200:
        print(f"Error: {res.status}: {res.read}")
        return "XXX"
    members = res.dict['Members']
    for m in members:
        res = rfo.get(m['@odata.id'])
        if res.status != 200:
            print(f"Member Error: {res.status}: {res.read}")
            return "XXX"
        nic_names.append({res.dict['Name']})
    return nic_names
