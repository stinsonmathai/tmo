def set_dns(rfo, dns, api=1, unit=1):
    """Set Primary DNS Servers

    Parameters:
    rfo (object): Redfish session
    dns (array): List of DNS server IP addresses
    api (int): API version
    unit (int): Enumerated component unit

    Returns:
    str: iLO response status
    """

    body = dict(Ipv4PrimaryDNS=dns)
    res = rfo.patch(f"/redfish/v{api}/Systems/{unit}/bios/settings", body)
    if res.status != 200:
        print(f"HTTP Fail Status: {res.status} - {res.read}")
        return("XXX")
    return f"Success: {res.status} - {res.read}"

