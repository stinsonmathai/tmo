def reboot_server(rfo, api=1, unit=1):
    """" (str) Reboot server """
    body = dict(Action="ComputerSystem.Reset", ResetType="ForceRestart")
    res = rfo.post(f"/redfish/v{api}/Systems/{unit}/Actions/ComputerSystem.Reset/", body)
    if res.status != 200:
        print(f"Error: {res.status}: {res.read}")
        return "XXX"
    return f"Success: {res.status}: {res.read}"

