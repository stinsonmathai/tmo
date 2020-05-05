from rf.login import login


def get_firmware(un, pw, url, api=1, unit=1):
    """"
    (str) Firmware version of iLO
    """
    rfo = login(un, pw, url)
    res = rfo.get(f"/redfish/v{api}/managers/{unit}")
    print(f"Firmware: {res.dict['FirmwareVersion']}")
    rfo.logout()
