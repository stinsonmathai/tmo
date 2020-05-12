def get_bios(rfo, api=1, unit=1):
    """" (str) The BIOS Version. """
    res = rfo.get(f"/redfish/v{api}/Systems/{unit}")
    if res.status != 200:
        print(f"Error: {res.status}: {res.read}")
        return "XXX"
    return res.dict['BiosVersion']

#TODO: Check with TMO if we should be looking for the additional info about BIOS or is it just BIOS Version