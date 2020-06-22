def get_hostname(rfo, api=1, unit=1):
    """ Get host name

    Parameters:
    rfo (object): Redfish Client Login Object
    api (int): API Value
    unit (int): Unit Value

    Returns:
    str: hostname
    """
    res = rfo.get(f"/redfish/v{api}/systems/{unit}")
    if res.status != 200:
        print(f"Error: {res.status}: {res.read}")
        return "XXX"
    return res.dict['HostName']

