def get_mem_blob(rfo, api=1, unit=1):
    """Aggregate memory DIMM information

    Parameters:
    rfo (object): Redfish Client Login Object
    api (int): API Value
    unit (int): Unit Value

    Returns:
    list: JSON
    """
    blob = []
    res = rfo.get(f"/redfish/v{api}/Systems/{unit}/Memory")
    if res.status != 200:
        print(f"Error: {res.status}: {res.read}")
        return "XXX"
    members = res.dict['Members']
    for m in members:
        res = rfo.get(m['@odata.id'])
        if res.status != 200:
            print(f"Member Error: {res.status}: {res.read}")
            return "XXX"
        blob.append(res.dict)
    return blob

