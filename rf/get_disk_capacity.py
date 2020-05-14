
def get_disk_capacity(rfo, api=1, unit=1):
    """
        This function fetches the Disk Capacity of the server.
        URL is https://IP_ADDRESS/redfish/v1/chassis/1/
        Information is in the following JSON snippet.
            "Links": {
                "Drives":}

        NOTE: There could be multiple drives in the server.

            Parameters:
            object: Redfish Client Login Object
            int: API Value
            int: Unit Value

            Returns:
            Integer: Combined Disk Capacity (Bytes)
    """

    blob = ""
    disk_capacity_total = 0
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
            f"Disk {d['@odata.id']} Capacity Bytes: {res.dict['CapacityBytes']}\n")

        disk_capacity_total = disk_capacity_total + int(res.dict['CapacityBytes'])
    print(disk_capacity_total) #FIXME:  remove this and return the proper value. Also fix the help string above.
    return blob


#TODO: DO we need to output the sum or the individual values?
