from rf.login import login
import json


def enable_sriov(un, pw, url, enable="Enabled", api=1, unit=1):
    """"
    (str) Enable SRIOV
    """
    rfo = login(un, pw, url)

    body = dict()
    body["Attributes"] = dict()
    body["Attributes"]["Sriov"] = enable

    res = rfo.patch(f"/redfish/v{api}/Systems/{unit}/bios/settings", body)
    print(f"Status: {res.status}")
    print(f"Status: {json.dumps(res.dict)}")


