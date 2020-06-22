def set_virtualization(rfo, mode, api=1, unit=1):
    """Enable processor hypervisor virtualization

    Parameters:
    rfo (object): Redfish login session
    mode (str): Enabled, Disabled
    api (int): API version
    unit (int): Enumerated component unit

    Returns:
    str: iLO response status
    """
    body = {'ProcVirtualization': mode}
    # res = rfo.patch(f"/redfish/v{api}/Systems/{unit}/bios/settings", body)
    res = rfo.patch(f"/redfish/v{api}/Systems/{unit}/bios/settings", body=body)
    if res.status != 200:
        print(f"HTTP Fail Status: {res.status} - {res.read}")
        return "XXX"
    return f"Success: {res.status} - {res.read}"
