import json


def get_mem_blob(rfo, api=1, unit=1):
    """Display aggregate memory information

    Parameters:
    rfo (object): Redfish Client Login Object
    api (int): API Value
    unit (int): Unit Value

    Returns:
    list: JSON
    """
    blob = []
    res = rfo.get(f"/redfish/v{api}/systems/{unit}")
    if res.status != 200:
        print(f"Error: {res.status}: {res.read}")
        return "XXX"
    blob.append(res.dict['MemorySummary'])
    res = rfo.get(f"/redfish/v{api}/systems/{unit}/Memory")
    if res.status != 200:
        print(f"Error: {res.status}: {res.read}")
        return "XXX"
    for d in res.dict['Oem']['Hpe']['MemoryList']:
        blob.append(d)
    return blob

