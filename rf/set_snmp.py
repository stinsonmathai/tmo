def set_snmp(rfo, destinations, api=1, unit=1):
    """Set SNMP Alert Destinations

    Parameters:
    rfo (object): Redfish login session
    destinations (array): The IP address or FQDN of remote management system that receive SNMP alerts.
    api (int): API version
    unit (int): Enumerated component unit

    Returns:
    str: iLO response status
    """
    body = {'AlertDestinations': destinations}
    res = rfo.patch(f"/redfish/v{api}/Managers/{unit}/SnmpService", body=body)
    if res.status != 200:
        print(f"HTTP Fail Status: {res.status} - {res.read}")
        return "XXX"
    return f"Success: {res.status} - {res.read}"

