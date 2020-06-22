def create_user(rfo, username, password, role, api=1):
    """Create iLO user account

    Parameters:
    rfo (object): Redfish login session
    username (str): User name
    password (str): Password
    role (str): Administrator, ReadOnly or Operator

    Returns:
    str: iLO response status
    """
    body = {'UserName': username, 'Password': password, 'RoleId': role}
    # res = rfo.post(f"/redfish/v{api}/AccountService/Accounts", body)
    res = rfo.post(f"/redfish/v{api}/AccountService/Accounts", body=body)
    if res.status != 201:
        print(f"HTTP Fail Status: {res.status} - {res.read}")
        return "XXX"
    return f"Success: {res.status} - {res.read}"
