def set_dns(rfo, dns, api=1, unit=1):
    """" (str) Set DNS """
    body = dict(Ipv4PrimaryDNS=dns)
    res = rfo.patch(f"/redfish/v{api}/Systems/{unit}/bios/settings", body)
    if res.status != 200:
        print(f"HTTP Fail Status: {res.status}")
        return("XXX")
    return "Success: " + res.read
