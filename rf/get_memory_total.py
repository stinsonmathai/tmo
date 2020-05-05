from rf.login import login


def get_memory_total(un, pw, url, api=1, unit=1):
    """"
    (str) Total amount of memory in the system measured in GiB.
    """
    rfo = login(un, pw, url)
    res = rfo.get(f"/redfish/v{api}/systems/{unit}")
    print(f"Total Memory GB: {res.dict['MemorySummary']['TotalSystemMemoryGiB']}")
    rfo.logout()
