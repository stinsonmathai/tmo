from rf.login import login


def get_eth(un, pw, url, api=1, unit=1):
    """"
    (str) The chassis model number.
    """
    rfo = login(un, pw, url)
    res = rfo.get(f"/redfish/v{api}/Chassis/{unit}")
    data = res.dict['Model']
    rfo.logout()
    return data



