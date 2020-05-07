def get_nic_blob(rfo, category="Systems", api=1, unit=1):
    """" (str) Network interfaces """
    blob = ""
    res = rfo.get(f"/redfish/v{api}/{category}/{unit}/EthernetInterfaces")
    if res.status != 200:
        print(f"HTTP Fail Status: {res.status}")
        return("XXX")
    members = res.dict['Members']
    for m in members:
        res = rfo.get(m['@odata.id'])
        if res.status != 200:
            print(f"HTTP Member Fail Status: {res.status}")
            return ("XXX")
        blob = blob + (
            f"Ethernet Interface {m['@odata.id']} MAC Address: {res.dict['MACAddress']}\n"
            f"Ethernet Interface {m['@odata.id']} IP4 Addresses: {res.dict['IPv4Addresses']}\n"
            f"Ethernet Interface {m['@odata.id']} Name: {res.dict['Name']}\n"
            f"Ethernet Interface {m['@odata.id']} Interface Enabled: {res.dict['InterfaceEnabled']}\n"
            f"Ethernet Interface {m['@odata.id']} Link Status: {res.dict['LinkStatus']}\n"
            f"Ethernet Interface {m['@odata.id']} Link State: {res.dict['Status']['State']}\n"
            f"Ethernet Interface {m['@odata.id']} Link Health: {res.dict['Status']['Health']}\n"
            f"Ethernet Interface {m['@odata.id']} Name Servers: {res.dict['NameServers']}\n"
            f"Ethernet Interface {m['@odata.id']} Speed Mbps: {res.dict['SpeedMbps']}\n"
        )
    return blob

