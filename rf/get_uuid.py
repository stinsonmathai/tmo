from rf.login import login


def get_uuid(un, pw, url, api=1, unit=1):
    """"
    (str) The universal unique identifier for this system
    """
    rfo = login(un, pw, url)
    res = rfo.get(f"/redfish/v{api}/systems/{unit}")
    print(f"UUID: {res.dict['UUID']}")
    rfo.logout()
