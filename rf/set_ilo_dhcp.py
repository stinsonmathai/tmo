def set_ilo_dhcp(rfo, dhcp=True, api=1, unit=1):
    """Enable or disable dhcp on dedicated iLO port

    Parameters:
    rfo (object): Redfish login session
    dhcp (array): True, False
    api (int): API version
    unit (int): Enumerated component unit

    Returns:
    str: iLO response status
    """

    if dhcp:
        body = {"DHCPv4": {"DHCPEnabled": True,
                           "UseDNSServers": True,
                           "UseDomainName": True,
                           "UseGateway": True,
                           "UseNTPServers": True,
                           "UseStaticRoutes": True
                           }}
    else:
        body = {"DHCPv4": {"DHCPEnabled": False,
            "UseDNSServers": False,
            "UseDomainName": False,
            "UseGateway": False,
            "UseNTPServers": False,
            "UseStaticRoutes": False
        }}

    res = rfo.patch(f"/redfish/v{api}/Managers/{unit}/EthernetInterfaces/1", body=body)
    if res.status != 200:
        print(f"HTTP Fail Status: {res.status} - {res.read}")
        return "XXX"
    return f"Success: {res.status} - {res.read}"

