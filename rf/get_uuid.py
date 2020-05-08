def get_uuid(rfo, api=1, unit=1):
    """" (str) The universal unique identifier for this system """
    res = rfo.get(f"/redfish/v{api}/systems/{unit}")
    if res.status != 200:
        print(f"Error: {res.status}: {res.read}")
        return "XXX"
    return res.dict['UUID']
