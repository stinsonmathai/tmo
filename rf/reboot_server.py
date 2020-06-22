def reboot_server(rfo, api=1, unit=1):
    """ Reboot server

    Parameters:
    rfo (object): Redfish Client Login Object
    api (int): API Value
    unit (int): Unit Value

    Returns:
    str: Reboot status
    """

    res = rfo.get(f"/redfish/v{api}/managers/{unit}")
    if "iLO 4" in res.dict['FirmwareVersion']:
        url = f"/redfish/v{api}/systems/{unit}"
        body = dict(Action="Reset", ResetType="ForceRestart")
    else:
        url = f"/redfish/v{api}/Systems/{unit}/Actions/ComputerSystem.Reset/"
        body = dict(Action="ComputerSystem.Reset", ResetType="ForceRestart")

    # res = rfo.post(url, body)
    res = rfo.post(url, body=body)
    if res.status != 200:
        print(f"Error: {res.status}: {res.read}")
        return "XXX"
    return f"Success: {res.status}: {res.read}"

