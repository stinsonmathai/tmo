from rf.login import login


def get_network_adapters_blob(un, pw, url, api=1, unit=1):
    """"
    (str) Network Interface Information
    """
    rfo = login(un, pw, url)
    res = rfo.get(f"/redfish/v{api}/Chassis/{unit}/NetworkAdapters")
    members = res.dict['Members']
    for m in members:
        res = rfo.get(m['@odata.id'])
        print(f"Adapter {m['@odata.id']} Model: {res.dict['Model']}")
        print(f"Adapter {m['@odata.id']} Part Number: {res.dict['PartNumber']}")
        print(f"Adapter {m['@odata.id']} Serial Number: {res.dict['SerialNumber']}")
        ports = res.dict['NetworkPorts']
        for p in ports:
            res = rfo.get(p['@odata.id'])
            devices = res.dict['Members']
            for d in devices:
                res = rfo.get(d['@odata.id'])
                print(f"Port {d['@odata.id']} Link Status: {res.dict['LinkStatus']}")
                print(f"Port {d['@odata.id']} Name: {res.dict['Name']}")
                print(f"Port {d['@odata.id']} Physical Port Number: {res.dict['PhysicalPortNumber']}")
                print(f"Port {d['@odata.id']} Signal Detected: {res.dict['SignalDetected']}")
                print(f"Port {d['@odata.id']} Capable Link Speed: {res.dict['SupportedLinkCapabilities'][0]['CapableLinkSpeedMbps']}")
                print(f"Port {d['@odata.id']} Link Technology: {res.dict['SupportedLinkCapabilities'][0]['LinkNetworkTechnology']}")

    rfo.logout()



