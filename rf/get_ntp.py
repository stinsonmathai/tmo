def get_ntp(rfo, api=1, unit=1):
    """Get NTP

    Parameters:
    rfo (object): Redfish Client Login Object
    api (int): API Value
    unit (int): Unit Value

    Returns:
    str: NTP Array
    """
    res = rfo.get(f"/redfish/v{api}/Managers/{unit}/datetime")
    if res.status != 200:
        print(f"Error: {res.status}: {res.read}")
        return "XXX"
    return res.dict['StaticNTPServers']

