def get_model(rfo, api=1, unit=1):
    """" (str) The chassis model number. """
    res = rfo.get(f"/redfish/v{api}/Chassis/{unit}")
<<<<<<< HEAD
    if res.status != 200:
        print(f"Error: {res.status}: {res.read}")
        return "XXX"
    return res.dict['Model']
=======
    # Add the error response if the response is not 200 OK
    print(f"Model Description: {res.dict['Model']}")
    rfo.logout()
>>>>>>> upstream/master
