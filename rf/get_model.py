
def get_model(rfo, api=1, unit=1):
    """
    This function fetches the MODEL of the server.
    URL is https://IP_ADDRESS/redfish/v1/systems/1/
    MODEL information is at the top level of the JSON Hierarchy

        Parameters:
        object: Redfish Client Login Object
        int: API Value
        int: Unit Value

        Returns:
        string: Model Info
    """
    res = rfo.get(f"/redfish/v{api}/Chassis/{unit}")
    if res.status != 200:
        print(f"Error: {res.status}: {res.read}")
        return "XXX"
    return res.dict['Model']

