def install_os(rfo, iso_url, api=1, unit=1):
    """ Install OS from HTTP ISO, Kickstart

    ISO must be customized to point to Kickstart file in same URL location

    Parameters:
    rfo (object): Redfish login session
    iso_url (str): HTTP location of ISO
    api (int): API version
    unit (int): Enumerated component unit

    Returns:
    str: iLO response status
    """

    # Eject any existing media
    body = {}
    # res = rfo.post(f"/redfish/v{api}/Managers/{unit}/VirtualMedia/2/Actions/Oem/Hpe/HpeiLOVirtualMedia.EjectVirtualMedia", body)
    res = rfo.post(f"/redfish/v{api}/Managers/{unit}/VirtualMedia/2/Actions/Oem/Hpe/HpeiLOVirtualMedia.EjectVirtualMedia", body=body)
    if res.status != 200:
        print(f"Error Eject: {res.status}: {res.read}")
        return "XXX"

    # Insert ISO image URL and set boot on reset
    body = {"Image": iso_url}
    # res = rfo.post(f"/redfish/v{api}/Managers/{unit}/VirtualMedia/2/Actions/Oem/Hpe/HpeiLOVirtualMedia.InsertVirtualMedia", body)
    res = rfo.post(f"/redfish/v{api}/Managers/{unit}/VirtualMedia/2/Actions/Oem/Hpe/HpeiLOVirtualMedia.InsertVirtualMedia", body=body)
    if res.status != 200:
        print(f"Error Insert: {res.status}: {res.read}")
        return "XXX"
    patch_body = {}
    patch_body["Oem"] = {"Hpe": {"BootOnNextServerReset": True}}
    # res = rfo.patch(f"/redfish/v{api}/Managers/{unit}/VirtualMedia/2/", patch_body)
    res = rfo.patch(f"/redfish/v{api}/Managers/{unit}/VirtualMedia/2/", body=patch_body)
    if res.status != 200:
        print(f"Error Boot: {res.status}: {res.read}")
        return "XXX"

    # Reset to install
    url = f"/redfish/v{api}/Systems/{unit}/Actions/ComputerSystem.Reset/"
    body = dict(Action="ComputerSystem.Reset", ResetType="ForceRestart")
    res = rfo.post(url, body)
    if res.status != 200:
        print(f"Error: {res.status}: {res.read}")
        return "XXX"
    return f"Success: {res.status}: {res.read}"

