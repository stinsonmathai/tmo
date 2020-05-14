def set_jitter(rfo, mode, api=1, unit=1):
    """Set processor jitter control

    Parameters:
    rfo (object): Redfish login session
    mode (str): Disabled, Auto-tuned, Manual-tuned
    api (int): API version
    unit (int): Enumerated component unit

    Returns:
    str: iLO response status
    """
    body = {'ProcessorJitterControl': mode}
    res = rfo.patch(f"/redfish/v{api}/Systems/{unit}/bios/settings", body)
    if res.status != 200:
        print(f"HTTP Fail Status: {res.status} - {res.read}")
        return "XXX"
    return f"Success: {res.status} - {res.read}"
