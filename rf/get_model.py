def get_model(rfo, api=1, unit=1):
    """" (str) The chassis model number. """
    res = rfo.get(f"/redfish/v{api}/Chassis/{unit}")
    if res.status != 200:
        print(f"Error: {res.status}: {res.read}")
        return "XXX"
    return res.dict['Model']
