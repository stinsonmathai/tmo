from rf.login import login


def get_model(un, pw, url, api=1, unit=1):
    """"
    (str) The chassis model number.
    """
    rfo = login(un, pw, url)
    res = rfo.get(f"/redfish/v{api}/Chassis/{unit}")
    print(f"Model Description: {res.dict['Model']}")
    rfo.logout()
