def get_tag(rfo, api=1, unit=1):
    """" (str) The Processor Type. """
    res = rfo.get(f"/redfish/v{api}/Systems/{unit}")
    if res.status != 200:
        print(f"Error: {res.status}: {res.read}")
        return "XXX"
    return res.dict['AssetTag']

#TODO: Check with TMO if we should be checking Asset Tag and what if this is BLANK
