def set_hostname(rfo, hostname, api=1, unit=1):
    """Set iLO hostname

    Parameters:
    rfo (object): Redfish login session
    hostname (str): Host name
    api (int): API version
    unit (int): Enumerated component unit

    Returns:
    str: iLO response status
    """
    body = dict(HostName=hostname)
    res = rfo.patch(f"/redfish/v{api}/Systems/{unit}", body)
    if res.status != 200:
        print(f"Error: {res.status}: {res.read}")
        return "XXX"
    return f"Success: {res.status}: {res.read}"
