from rf.login import login


def get_disk_blob(un, pw, url, api=1, unit=1):
    """"
    (str) Disk drives information
    """
    rfo = login(un, pw, url)
    res = rfo.get(f"/redfish/v{api}/Chassis/{unit}")
    members = res.dict['Links']['Drives']
    for d in members:
        res = rfo.get(d['@odata.id'])
        print(f"Disk {d['@odata.id']} Capacity Bytes: {res.dict['CapacityBytes']}")
        print(f"Disk {d['@odata.id']} Media Type: {res.dict['MediaType']}")
        print(f"Disk {d['@odata.id']} Model: {res.dict['Model']}")
        print(f"Disk {d['@odata.id']} Location Box:Bay: {res.dict['Location'][0]['Info']}")
        print(f"Disk {d['@odata.id']} Name: {res.dict['Name']}")
        print(f"Disk {d['@odata.id']} Oem Drive Status: {res.dict['Oem']['Hpe']['DriveStatus']['Health']}")
        print(f"Disk {d['@odata.id']} Oem Temperature Status: {res.dict['Oem']['Hpe']['TemperatureStatus']['Health']}")
        print(f"Disk {d['@odata.id']} Oem Power On Hours: {res.dict['Oem']['Hpe']['PowerOnHours']}")
        print(f"Disk {d['@odata.id']} Oem Wear Status: {res.dict['Oem']['Hpe']['WearStatus']}")
        print(f"Disk {d['@odata.id']} Life Percent: {res.dict['PredictedMediaLifeLeftPercent']}")
        print(f"Disk {d['@odata.id']} SerialNumber: {res.dict['SerialNumber']}")
        print(f"Disk {d['@odata.id']} Status: {res.dict['Status']['Health']}")
    rfo.logout()



