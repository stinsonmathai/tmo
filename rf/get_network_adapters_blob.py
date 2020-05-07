def get_network_adapters_blob(rfo, api=1, unit=1):
    """" (str) Network Interface Information """
    blob = ""
    res = rfo.get(f"/redfish/v{api}/Chassis/{unit}/NetworkAdapters")
    members = res.dict['Members']
    for m in members:
        res = rfo.get(m['@odata.id'])
        if res.status != 200:
            print(f"HTTP Fail Status: {res.status}")
            return ("XXX")
        ports = res.dict['NetworkPorts']
        for p in ports:
            res = rfo.get(p['@odata.id'])
            if res.status != 200:
                print(f"HTTP Ports Fail Status: {res.status}")
                return ("XXX")
            devices = res.dict['Members']
            for d in devices:
                res = rfo.get(d['@odata.id'])
                if res.status != 200:
                    print(f"HTTP Devices Fail Status: {res.status}")
                    return ("XXX")
            blob = blob + (
                f"Port {d['@odata.id']} Link Status: {res.dict['LinkStatus']}\n"
                f"Port {d['@odata.id']} Name: {res.dict['Name']}\n"
                f"Port {d['@odata.id']} Physical Port Number: {res.dict['PhysicalPortNumber']}\n"
                f"Port {d['@odata.id']} Signal Detected: {res.dict['SignalDetected']}\n"
                f"Port {d['@odata.id']} Capable Link Speed: {res.dict['SupportedLinkCapabilities'][0]['CapableLinkSpeedMbps']}\n"
                f"Port {d['@odata.id']} Link Technology: {res.dict['SupportedLinkCapabilities'][0]['LinkNetworkTechnology']}\n"
            )
    return blob

