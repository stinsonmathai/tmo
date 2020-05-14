def get_status(rfo, api=1, unit=1):
    """This function fetches the Health Status of the server.
    URL is https://IP_ADDRESS/redfish/v1/systems/1/
    Information is in the following JSON snippet.
    "Status": {
        "Health":}

    Parameters:
    rfo (object): Redfish Client Login Object
    api (int): API Value
    unit (int): Unit Value

    Returns:
    str: Health Status
    """
    res = rfo.get(f"/redfish/v{api}/Systems/{unit}")
    if res.status != 200:
        print(f"Error: {res.status}: {res.read}")
        return "XXX"
    return res.dict['Status']['Health']
