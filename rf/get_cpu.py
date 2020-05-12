def get_cpu(rfo, api=1, unit=1):
    """" (str) The Processor Type. """
    res = rfo.get(f"/redfish/v{api}/Systems/{unit}")
    if res.status != 200:
        print(f"Error: {res.status}: {res.read}")
        return "XXX"
    return res.dict['ProcessorSummary']['Model']

#TODO: Check with TMO if we should be checking for multiple processors and if they match.
