def enable_sriov(rfo, enable="Enabled", api=1, unit=1):
    """Enable SRIOV

    Parameters:
    rfo (object): Redfish login session
    enable (str): Enabled, Disabled
    api (int): API Value
    unit (int): Unit Value

    Returns:
    str: iLO response status
    """
    body = dict()
    body["Attributes"] = dict()
    body["Attributes"]["Sriov"] = enable
    # res = rfo.patch(f"/redfish/v{api}/Systems/{unit}/bios/settings", body)
    res = rfo.patch(f"/redfish/v{api}/Systems/{unit}/bios/settings", body=body)
    if res.status != 200:
        print(f"Error: {res.status}: {res.read}")
        return "XXX"
    return f"Success: {res.status}: {res.read}"

