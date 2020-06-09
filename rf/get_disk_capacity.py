
def get_disk_capacity(rfo, api=1, unit=1):
    """ Disk capacity of each drive in server

    Parameters:
    rfo (object): Redfish Client Login Object
    api (int): API Value
    unit (int): Unit Value

    Returns:
    list: Drive capacity
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
    # disk_capacity_total = 0
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
            # disk_capacity_total = disk_capacity_total + int(res.dict['CapacityBytes'])
        # print(disk_capacity_total) #FIXME:  remove this and return the proper value. Also fix the help string above.

    return blob

#TODO: DO we need to output the sum or the individual values?
