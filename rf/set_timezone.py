def set_timezone(rfo, tz, api=1, unit=1):
    """" (str) Set Timezone """
    body = dict(TimeZone=tz)
    res = rfo.patch(f"/redfish/v{api}/Systems/{unit}/bios/settings", body)
    if res.status != 200:
        print(f"HTTP Fail Status: {res.status}")
        return("XXX")
    return "Success: " + res.read
