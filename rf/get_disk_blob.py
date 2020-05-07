def get_disk_blob(rfo, api=1, unit=1):
    """" (str) Disk drives information """
    blob = ""
    res = rfo.get(f"/redfish/v{api}/Chassis/{unit}")
    if res.status != 200:
        print(f"HTTP Fail Status: {res.status}")
        return("XXX")
    members = res.dict['Links']['Drives']
    for d in members:
        res = rfo.get(d['@odata.id'])
        if res.status != 200:
            print(f"HTTP Members Status: {res.status}")
            return ("XXX")
        blob = blob + (
            f"Disk {d['@odata.id']} Capacity Bytes: {res.dict['CapacityBytes']}\n"
            f"Disk {d['@odata.id']} Media Type: {res.dict['MediaType']}n"
            f"Disk {d['@odata.id']} Model: {res.dict['Model']}\n"
            f"Disk {d['@odata.id']} Location Box:Bay: {res.dict['Location'][0]['Info']}n"
            f"Disk {d['@odata.id']} Name: {res.dict['Name']}\n"
            f"Disk {d['@odata.id']} Oem Drive Status: {res.dict['Oem']['Hpe']['DriveStatus']['Health']}\n"
            f"Disk {d['@odata.id']} Oem Temperature Status: {res.dict['Oem']['Hpe']['TemperatureStatus']['Health']}n"
            f"Disk {d['@odata.id']} Oem Power On Hours: {res.dict['Oem']['Hpe']['PowerOnHours']}n"
            f"Disk {d['@odata.id']} Oem Wear Status: {res.dict['Oem']['Hpe']['WearStatus']}\n"
            f"Disk {d['@odata.id']} Life Percent: {res.dict['PredictedMediaLifeLeftPercent']}\n"
            f"Disk {d['@odata.id']} SerialNumber: {res.dict['SerialNumber']}\n"
            f"Disk {d['@odata.id']} Status: {res.dict['Status']['Health']}\n"
        )
    return blob



