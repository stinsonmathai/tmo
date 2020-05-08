def set_power_options(rfo, mode, api=1, unit=1):
    """" (str) Set Timezone """
    body = dict(RedundantPowerSupply=mode)
    res = rfo.patch(f"/redfish/v{api}/Systems/{unit}/bios/settings", body)
    if res.status != 200:
        print(f"HTTP Fail Status: {res.status}")
        return("XXX")
    return "Success: " + res.read
