def set_hostname(rfo, hostname, api=1, unit=1):
    """" (str) Set hostname """
    body = dict()
    body["HostName"] = hostname
    res = rfo.patch(f"/redfish/v{api}/Systems/{unit}", body)
    if res.status != 200:
        print(f"HTTP Fail Status: {res.status}")
        return("XXX")
    return "Success"
