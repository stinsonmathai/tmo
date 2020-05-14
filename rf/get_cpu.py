
def get_cpu(rfo, api=1, unit=1):
    """
    This function fetches the CPU model of the server.
    URL is https://IP_ADDRESS/redfish/v1/systems/1/
    Information is in the following JSON snippet.
    "ProcessorSummary": {
        "Model" }

    Parameters:
    object: Redfish Client Login Object
    int: API Value
    int: Unit Value

    Returns:
    string: CPU Model
    """

    res = rfo.get(f"/redfish/v{api}/Systems/{unit}")
    if res.status != 200:
        print(f"Error: {res.status}: {res.read}")
        return "XXX"
    return res.dict['ProcessorSummary']['Model']


