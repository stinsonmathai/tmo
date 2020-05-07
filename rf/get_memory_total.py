def get_memory_total(rfo, api=1, unit=1):
    """" (str) Total amount of memory in the system measured in GiB. """
    res = rfo.get(f"/redfish/v{api}/systems/{unit}")
    if res.status != 200:
        print(f"HTTP Fail Status: {res.status}")
        return("XXX")
    return res.dict['MemorySummary']['TotalSystemMemoryGiB']
