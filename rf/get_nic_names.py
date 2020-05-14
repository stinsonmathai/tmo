


def get_nic_names(rfo, api=1, unit=1):
    """
    This function fetches the names of the NICS on the server.
    URL is https://IP_ADDRESS/redfish/v1/systems/1/
    MODEL information is at the top level of the JSON Hierarchy

        Parameters:
        object: Redfish Client Login Object
        int: API Value
        int: Unit Value

        Returns:
        list: names of the NICS on the server
    """
    nic_names = []
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
        nic_names.append({res.dict['Name']}) #TODO: look at why this is a dictionary and not an element
    return nic_names
