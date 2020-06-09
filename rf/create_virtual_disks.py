def create_virtual_disks(rfo, raid=None, api=1, unit=1):
    """Enable raid

    Parameters:
    rfo (object): Redfish login session
    raid (dictionary): Raid configuration
    api (int): API version
    unit (int): Enumerated component unit

    Returns:
    str: iLO response status
    """

    if raid is None:
        raid = {
            "DataGuard": "Disabled",
            "LogicalDrives": [
               {
                  "CapacityGiB": 260,
                  "Raid": "Raid1",
                  "LogicalDriveName": "MyLD",
                  "DataDrives": [
                        "1I:1:1",
                        "1I:1:2"
                  ],
                  # "Accelerator": "ControllerCache" # Requires redundant power
               }
            ]
        }

    res = rfo.put(f"/redfish/v{api}/Systems/{unit}/smartstorageconfig1/settings", raid)
    if res.status != 200:
        print(f"HTTP Fail Status: {res.status} - {res.read}")
        return "XXX"
    return f"Success: {res.status} - {res.read}"


