def set_turbo(rfo, mode, api=1, unit=1):
    """Set processor turbo boost technology

    Parameters:
    rfo (object): Redfish login session
    mode (str): Enabled, Disabled
    api (int): API version
    unit (int): Enumerated component unit

    Returns:
    str: iLO response status
    """
    body = {'Attributes': {'ProcTurbo': mode}}
    res = rfo.patch(f"/redfish/v{api}/Systems/{unit}/bios/settings", body=body)
    if res.status != 200:
        print(f"HTTP Fail Status: {res.status} - {res.read}")
        return "XXX"
    return f"Success: {res.status} - {res.read}"

