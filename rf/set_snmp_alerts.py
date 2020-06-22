def set_snmp_alerts(rfo, alert, communities, api=1, unit=1):
    """Set SNMP enable alerts and read communities

    Parameters:
    rfo (object): Redfish login session
    alert (boolean): Enable alerts
    community (array): SNMP read communities
    api (int): API version
    unit (int): Enumerated component unit

    Returns:
    str: iLO response status
    """
    body = {'AlertsEnabled': alert, 'ReadCommunities': communities}
    # res = rfo.patch(f"/redfish/v{api}/Managers/{unit}/SnmpService", body)
    res = rfo.patch(f"/redfish/v{api}/Managers/{unit}/SnmpService", body=body)
    if res.status != 200:
        print(f"HTTP Fail Status: {res.status} - {res.read}")
        return "XXX"
    return f"Success: {res.status} - {res.read}"

