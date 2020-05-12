def create_user(rfo, username, password, role, api=1, unit=1):
    """Create iLO user account

    Parameters:
    rfo (object): Redfish login session
    username (str): User name
    password (str): Password
    role (str): Administrator, ReadOnly or Operator

    Returns:
    str: iLO response status
    """
    # TODO: This doesn't work yet
    body = {'StaticNTPServers': ntp}
    res = rfo.patch(f"/redfish/v{api}/Managers/{unit}/datetime", body)
    if res.status != 200:
        print(f"HTTP Fail Status: {res.status} - {res.read}")
        return "XXX"
    return f"Success: {res.status} - {res.read}"
