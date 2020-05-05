from rf.login import login
import json


def reboot_server(un, pw, url, api=1, unit=1):
    """"
    (str) Reboot server
    """
    rfo = login(un, pw, url)

    body = dict()
    body["Action"] = "ComputerSystem.Reset"
    body["ResetType"] = "ForceRestart"

    res = rfo.post(f"/redfish/v{api}/Systems/{unit}/Actions/ComputerSystem.Reset/", body)
    print(f"Status: {res.status}")
    print(f"Status: {json.dumps(res.dict)}")

