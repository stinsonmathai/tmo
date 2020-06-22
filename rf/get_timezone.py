def get_timezone(rfo, api=1, unit=1):
    """ Get timezone

    Parameters:
    rfo (object): Redfish Client Login Object
    api (int): API Value
    unit (int): Unit Value

    Returns:
    str: timezone
    """
    res = rfo.get(f"/redfish/v{api}/systems/{unit}/bios")
    if res.status != 200:
        print(f"Error: {res.status}: {res.read}")
        return "XXX"
    return res.dict['Attributes']['TimeZone']

