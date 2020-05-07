def get_disk_capacity(rfo, api=1, unit=1):
    """" (str) Disk drive capacity """
    blob = ""
    res = rfo.get(f"/redfish/v{api}/Chassis/{unit}")
    if res.status != 200:
        print(f"HTTP Fail Status: {res.status}")
        return("XXX")
    members = res.dict['Links']['Drives']
    for d in members:
        res = rfo.get(d['@odata.id'])
        if res.status != 200:
            print(f"HTTP Members Fail Status: {res.status}")
            return ("XXX")
        blob = blob + (
            f"Disk {d['@odata.id']} Capacity Bytes: {res.dict['CapacityBytes']}\n"
        )
    return blob



