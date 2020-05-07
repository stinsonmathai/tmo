def get_model(rfo, api=1, unit=1):
    """" (str) The chassis model number. """
    res = rfo.get(f"/redfish/v{api}/Chassis/{unit}")
    if res.status != 200:
        print(f"HTTP Fail Status: {res.status}")
        return("XXX")
    return res.dict['Model']
