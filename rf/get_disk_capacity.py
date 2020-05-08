def get_disk_capacity(rfo, api=1, unit=1):
    """" (str) Disk drive capacity """
    blob = ""
    res = rfo.get(f"/redfish/v{api}/Chassis/{unit}")
    if res.status != 200:
        print(f"Error: {res.status}: {res.read}")
        return "XXX"
    members = res.dict['Links']['Drives']
    for d in members:
        res = rfo.get(d['@odata.id'])
        if res.status != 200:
            print(f"Member Error: {res.status}: {res.read}")
            return "XXX"
        blob = blob + (
            f"Disk {d['@odata.id']} Capacity Bytes: {res.dict['CapacityBytes']}\n"
        )
    return blob



