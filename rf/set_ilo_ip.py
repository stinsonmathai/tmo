def set_ilo_ip(rfo, ip=None, api=1, unit=1):
    """Set iLO static IPv4 address information

    Parameters:
    rfo (object): Redfish login session
    ip (array): array/dict of ip addresses
    api (int): API version
    unit (int): Enumerated component unit

    Returns:
    str: iLO response status
    """

    if ip is None:
        ip = {"IPv4Addresses": [{
            "Address": "16.91.158.182",
            "Gateway": "16.91.152.1",
            "SubnetMask": "255.255.248.0"}]}

    res = rfo.patch(f"/redfish/v{api}/Managers/{unit}/EthernetInterfaces/1", body=ip)
    if res.status != 200:
        print(f"HTTP Fail Status: {res.status} - {res.read}")
        return "XXX"
    return f"Success: {res.status} - {res.read}"

