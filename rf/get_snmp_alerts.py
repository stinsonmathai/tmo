def get_snmp_alerts(rfo, api=1, unit=1):
    """Get SNMP alerts

    Parameters:
    rfo (object): Redfish Client Login Object
    api (int): API Value
    unit (int): Unit Value

    Returns:
    str: SNMP alerts
    """
    res = rfo.get(f"/redfish/v{api}/Managers/{unit}/SnmpService")
    if res.status != 200:
        print(f"Error: {res.status}: {res.read}")
        return "XXX"
    return str(res.dict['AlertsEnabled']) + " " + str(res.dict['ReadCommunities'])

