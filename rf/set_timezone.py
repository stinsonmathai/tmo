def set_timezone(rfo, tz, api=1, unit=1):
    """Set iLO timezone

    Parameters:
    rfo (object): Redfish login session
    tz (str): TODO: Available timezones
    api (int): API version
    unit (int): Enumerated component unit

    Returns:
    str: iLO response status
    """
    body = dict(TimeZone=tz)
    res = rfo.patch(f"/redfish/v{api}/Systems/{unit}/bios/settings", body)
    if res.status != 200:
        print(f"HTTP Fail Status: {res.status} - {res.read}")
        return("XXX")
    return "Success: " + res.read
