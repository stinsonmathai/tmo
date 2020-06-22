def get_snmp(rfo, api=1, unit=1):
    """Get SNMP

    Parameters:
    rfo (object): Redfish Client Login Object
    api (int): API Value
    unit (int): Unit Value

    Returns:
    str: SNMP
    """
    res = rfo.get(f"/redfish/v{api}/Managers/{unit}/SnmpService")
    if res.status != 200:
        print(f"Error: {res.status}: {res.read}")
        return "XXX"
    return res.dict['AlertDestinations']

