
def get_disk_count(rfo, api=1, unit=1):
    """ This function fetches the number of disks in the server.
    URL is https://IP_ADDRESS/redfish/v1/chassis/1/
    Information is in the following JSON snippet.
     "Links": {
        "Drives":}

    Parameters:
    rfo (object): Redfish Client Login Object
    api (int): API Value
    api (int): Unit Value

    Returns:
    int: disk count
    """
    res = rfo.get(f"/redfish/v{api}/Chassis/{unit}")
    members = res.dict['Links']['Drives']
    if res.status != 200:
        print(f"Error: {res.status}: {res.read}")
        return "XXX"
    return int(len(members))
