def set_timezone(rfo, tz, api=1, unit=1):
    """Set iLO timezone

    Parameters:
    rfo (object): Redfish login session
    tz (str): Examples: UtcM10:UTC-10:00, Hawaii
                        UtcM8:UTC-08:00, Pacific Time(US & Canada)
                        UtcM7:UTC-07:00, Mountain Time (US & Canada)
                        UtcM6:UTC-06:00, Central America, Central Time(US & Canada)
                        UtcM5:UTC-05:00, Eastern Time(US & Canada)
    api (int): API version
    unit (int): Enumerated component unit

    Returns:
    str: iLO response status
    """
    body = dict(TimeZone=tz)
    # res = rfo.patch(f"/redfish/v{api}/Systems/{unit}/bios/settings", body)
    res = rfo.patch(f"/redfish/v{api}/Systems/{unit}/bios/settings", body=body)
    if res.status != 200:
        print(f"HTTP Fail Status: {res.status} - {res.read}")
        return("XXX")
    return f"Success: {res.status}: {res.read}"
