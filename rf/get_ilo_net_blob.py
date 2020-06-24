def get_ilo_net_blob(rfo, api=1, unit=1):
    """ Get ilo dedicate nic information

    Parameters:
    rfo (object): Redfish Client Login Object
    api (int): API Value
    unit (int): Unit Value

    Returns:
    dict: network blob
    """
    res = rfo.get(f"/redfish/v{api}/managers/1/ethernetinterfaces/1")
    if res.status != 200:
        print(f"Error: {res.status}: {res.read}")
        return "XXX"
    return res.dict

