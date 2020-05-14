def get_tag(rfo, api=1, unit=1):
    """This function fetches the ASSET TAG of the server.
    URL is https://IP_ADDRESS/redfish/v1/systems/1/
    Information is in the following JSON snippet.
    "AssetTag": ""

    Parameters:
    rfo (object): Redfish Client Login Object
    api (int): API Value
    unit (int): Unit Value

    Returns:
    str: Asset Tag
    """
    res = rfo.get(f"/redfish/v{api}/systems/{unit}")
    if res.status != 200:
        print(f"Error: {res.status}: {res.read}")
        return "XXX"
    return res.dict['AssetTag']

