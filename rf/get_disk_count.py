
def get_disk_count(rfo, api=1, unit=1):
    """ Number of physical drives in server

    Parameters:
    rfo (object): Redfish Client Login Object
    api (int): API Value
    unit (int): Unit Value

    Returns:
    int: Number of drives
    """

    blob = []

    # Smart Storage Drives
    res = rfo.get(f"/redfish/v{api}/Systems/{unit}/SmartStorage/ArrayControllers")
    if res.status != 200:
        print(f"Error: {res.status}: {res.read}")
        return "XXX"
    if res.dict['Members@odata.count']:
        for m in res.dict['Members']:
            res = rfo.get(m['@odata.id'])
            if res.status != 200:
                print(f"Member Error: {res.status}: {res.read}")
                return "XXX"
            res = rfo.get(res.dict['Links']['PhysicalDrives']['@odata.id'])
            if res.status != 200:
                print(f"Links Error: {res.status}: {res.read}")
                return "XXX"
            if res.dict['Members@odata.count']:
                for d in res.dict['Members']:
                    res = rfo.get(d['@odata.id'])
                    if res.status != 200:
                        print(f"Drive Error: {res.status}: {res.read}")
                        return "XXX"
                    blob.append(f"Disk {d['@odata.id']} Capacity GB: {res.dict['CapacityGB']}\n")

    # No controller
    res = rfo.get(f"/redfish/v{api}/Chassis/{unit}")
    if res.status != 200:
        print(f"Error: {res.status}: {res.read}")
        return "XXX"
    if 'Drives' in res.dict['Links']:
        members = res.dict['Links']['Drives']
        for d in members:
            res = rfo.get(d['@odata.id'])
            if res.status != 200:
                print(f"Member Error: {res.status}: {res.read}")
                return "XXX"
            blob.append(f"Disk {d['@odata.id']} Capacity Bytes: {res.dict['CapacityBytes']}\n")

    return len(blob)

