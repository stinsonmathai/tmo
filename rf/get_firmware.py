def get_firmware(rfo, api=1, unit=1):
    """This function fetches the FIRMWARE of the server.
    URL is https://IP_ADDRESS/redfish/v1/chassis/1/
    Information is in the following JSON snippet.
    OEM": {
        Hpe": {
            Firmware": {
                    "PlatformDefinitionTable": {
                        "Current": {
                            "VersionString"}}}}

    Parameters:
    rfo (object): Redfish Client Login Object
    api (int): API Value
    unit (int): Unit Value

    Returns:
    string: Firmware
    """
    res = rfo.get(f"/redfish/v{api}/managers/{unit}")
    if res.status != 200:
        print(f"Error: {res.status}: {res.read}")
        return "XXX"
    return res.dict['FirmwareVersion']
    # return res.dict['Oem']['Hpe']['Firmware']['PlatformDefinitionTable']['Current']['VersionString']
