def set_ntp(rfo, ntp, api=1, unit=1):
    """Set static NTP servers

    Parameters:
    rfo (object): Redfish login session
    ntp (array): Array of IP addresses
    api (int): API version
    unit (int): Enumerated component unit

    Returns:
    str: iLO response status
    """
    body = {'StaticNTPServers': ntp}
    # res = rfo.patch(f"/redfish/v{api}/Managers/{unit}/datetime", body)
    res = rfo.patch(f"/redfish/v{api}/Managers/{unit}/datetime", body=body)
    if res.status != 200:
        print(f"HTTP Fail Status: {res.status} - {res.read}")
        return "XXX"
    return f"Success: {res.status} - {res.read}"
