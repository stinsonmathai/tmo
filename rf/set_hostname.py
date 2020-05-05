from rf.login import login
import json


def set_hostname(un, pw, url, hostname, api=1, unit=1):
    """"
    (str) Set hostname
    """
    rfo = login(un, pw, url)

    body = dict()
    body["HostName"] = hostname

    res = rfo.patch(f"/redfish/v{api}/Systems/{unit}", body)
    print(f"Status: {res.status}")
    print(f"Status: {json.dumps(res.dict)}")


