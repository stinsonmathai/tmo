def set_hostname(rfo, hostname, api=1, unit=1):
    """" (str) Set hostname """
    body = dict(HostName=hostname)
    res = rfo.patch(f"/redfish/v{api}/Systems/{unit}", body)
    if res.status != 200:
        print(f"Error: {res.status}: {res.read}")
        return "XXX"
    return f"Success: {res.status}: {res.read}"
