def get_disk_count(rfo, api=1, unit=1):
    """" (str) Disk drive count """
    res = rfo.get(f"/redfish/v{api}/Chassis/{unit}")
    members = res.dict['Links']['Drives']
    if res.status != 200:
        print(f"HTTP Fail Status: {res.status}")
        return("XXX")
    return len(members)
