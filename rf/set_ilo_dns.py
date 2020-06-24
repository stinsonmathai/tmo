def set_ilo_dns(rfo, dns=None, api=1, unit=1):
    """Set DNS name servers

    Parameters:
    rfo (object): Redfish login session
    dns (array): Array of ip addresses
    api (int): API version
    unit (int): Enumerated component unit

    Returns:
    str: iLO response status
    """

    if dns is None:
        dns = ["16.110.135.52", "16.110.135.51"]

    body = {"StaticNameServers": dns}
    res = rfo.patch(f"/redfish/v{api}/Managers/{unit}/EthernetInterfaces/1", body=body)
    if res.status != 200:
        print(f"HTTP Fail Status: {res.status} - {res.read}")
        return "XXX"
    return f"Success: {res.status} - {res.read}"

