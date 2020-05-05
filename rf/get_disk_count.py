from rf.login import login


def get_disk_count(un, pw, url, api=1, unit=1):
    """"
    (str) Disk drive count
    """
    rfo = login(un, pw, url)
    res = rfo.get(f"/redfish/v{api}/Chassis/{unit}")
    members = res.dict['Links']['Drives']
    print(f"Disk Drive Count: {len(members)}")
    rfo.logout()



