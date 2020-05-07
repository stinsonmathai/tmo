#TODO:  This is not the correct firmware version.  This gets ilo fw version
def get_firmware(rfo, api=1, unit=1):
    """" (str) Firmware version of iLO """
    res = rfo.get(f"/redfish/v{api}/managers/{unit}")
    if res.status != 200:
        print(f"HTTP Fail Status: {res.status}")
        return("XXX")
    return res.dict['FirmwareVersion']
