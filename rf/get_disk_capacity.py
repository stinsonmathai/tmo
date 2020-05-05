from rf.login import login


def get_disk_capacity(un, pw, url, api=1, unit=1):
    """"
    (str) Disk drive capacity
    """
    rfo = login(un, pw, url)
    res = rfo.get(f"/redfish/v{api}/Chassis/{unit}")
    members = res.dict['Links']['Drives']
    for d in members:
        res = rfo.get(d['@odata.id'])
        print(f"Disk {d['@odata.id']} Capacity Bytes: {res.dict['CapacityBytes']}")
    rfo.logout()



