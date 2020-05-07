def enable_sriov(rfo, enable="Enabled", api=1, unit=1):
    """" (str) Enable SRIOV """
    body = dict()
    body["Attributes"] = dict()
    body["Attributes"]["Sriov"] = enable
    res = rfo.patch(f"/redfish/v{api}/Systems/{unit}/bios/settings", body)
    if res.status != 200:
        print(f"HTTP Fail Status: {res.status}")
        return ("XXX")
    return "Success"

