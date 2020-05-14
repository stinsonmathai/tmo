def set_power_options(rfo, mode, api=1, unit=1):
    """Set power mode options

    Parameters:
    rfo (object): Redfish login session
    mode (str): Power mode TODO: power modes available
    api (int): API version
    unit (int): Enumerated component unit

    Returns:
    str: iLO response status
    """
    body = dict(RedundantPowerSupply=mode)
    res = rfo.patch(f"/redfish/v{api}/Systems/{unit}/bios/settings", body)
    if res.status != 200:
        print(f"HTTP Fail Status: {res.status} - {res.read}")
        return("XXX")
    return f"Success: {res.status} - {res.read}"
