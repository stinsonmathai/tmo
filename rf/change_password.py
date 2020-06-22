def change_password(rfo, username, password, api=1):
    """Change iLO user account password

    Parameters:
    rfo (object): Redfish login session
    username (str): User name
    password (str): New password

    Returns:
    str: iLO response status
    """

    res = rfo.get(f"/redfish/v{api}/AccountService/Accounts")
    if res.status != 200:
        print(f"Error: {res.status}: {res.read}")
        return "XXX"
    members = res.dict['Members']
    for m in members:
        res = rfo.get(m['@odata.id'])
        if res.status != 200:
            print(f"Member {m} Error: {res.status}: {res.read}")
            return "XXX"
        if res.dict['UserName'] == username:
            body = {'Password': password}
            # res = rfo.patch(m['@odata.id'], body)
            res = rfo.patch(m['@odata.id'], body=body)
            if res.status != 200:
                print(f"HTTP Fail Status: {res.status} - {res.read}")
                return "XXX"
            return f"Success: {res.status} - {res.read}"

