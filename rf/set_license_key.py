#TODO: Do not test this on current lab box
def set_license_key(rfo, key, api=1, unit=1):
    """Set iLO license key

    Parameters:
    rfo (object): Redfish session
    key (str): License key
    api (int): API version
    unit (int): Enumerated component unit

    Returns:
    str: iLO response status
    """
    body = {'Oem': {'Hpe': {'LicenseKey': key}}}
    # res = rfo.patch(f"/redfish/v{api}/Managers/{unit}/DONOTTEST", body)
    res = rfo.patch(f"/redfish/v{api}/Managers/{unit}/DONOTTEST", body=body)
    if res.status != 200:
        print(f"HTTP Fail Status: {res.status} - {res.read}")
        return("XXX")
    return f"Success: {res.status} - {res.read}"
