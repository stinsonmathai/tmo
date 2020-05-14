def get_network_adapters_blob(rfo, api=1, unit=1):
    """Aggregate network adapter information

    Parameters:
    rfo (object): Redfish Client Login Object
    api (int): API Value
    unit (int): Unit Value

    Returns:
    list: JSON
    """
    blob = []
    res = rfo.get(f"/redfish/v{api}/Chassis/{unit}/NetworkAdapters")
    members = res.dict['Members']
    for m in members:
        res = rfo.get(m['@odata.id'])
        if res.status != 200:
            print(f"Error: {res.status}: {res.read}")
            return "XXX"
        ports = res.dict['NetworkPorts']
        for p in ports:
            res = rfo.get(p['@odata.id'])
            if res.status != 200:
                print(f"Port Error: {res.status}: {res.read}")
                return "XXX"
            devices = res.dict['Members']
            for d in devices:
                res = rfo.get(d['@odata.id'])
                if res.status != 200:
                    print(f"Device Error: {res.status}: {res.read}")
                    return "XXX"
            blob.append(res.dict)
    return blob

