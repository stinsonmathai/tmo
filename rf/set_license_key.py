#TODO: Do not test this on current lab box
def set_license_key(rfo, key, api=1, unit=1):
    """" (str) Set License Key """
    body = {'Oem': {'Hpe': {'LicenseKey': key}}}
    res = rfo.patch(f"/redfish/v{api}/Managers/{unit}/DONOTTEST", body)
    if res.status != 200:
        print(f"HTTP Fail Status: {res.status}")
        return("XXX")
    return "Success: " + res.read
