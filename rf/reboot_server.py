def reboot_server(rfo, api=1, unit=1):
    """" (str) Reboot server """
    body = dict()
    body["Action"] = "ComputerSystem.Reset"
    body["ResetType"] = "ForceRestart"
    res = rfo.post(f"/redfish/v{api}/Systems/{unit}/Actions/ComputerSystem.Reset/", body)
    if res.status != 200:
        print(f"HTTP Fail Status: {res.status}")
        return("XXX")
    return "Success"

