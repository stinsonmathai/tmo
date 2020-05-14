def get_memory_total(rfo, api=1, unit=1):
    """ This function fetches the TOTAL MEMORY installed in the server.
    URL is https://IP_ADDRESS/redfish/v1/systems/1/
    Information is in the following JSON snippet.
    "MemorySummary": {
        "TotalSystemMemoryGiB":}

    Parameters:
    rfo (object): Redfish Client Login Object
    api (int): API Value
    unit (int): Unit Value

    Returns:
    int: Total Memory
    """
    res = rfo.get(f"/redfish/v{api}/systems/{unit}")
    if res.status != 200:
        print(f"Error: {res.status}: {res.read}")
        return "XXX"
    return int(res.dict['MemorySummary']['TotalSystemMemoryGiB'])

