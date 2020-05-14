import json


def get_cpu_blob(rfo, api=1, unit=1):
    """Display aggregate CPU information

    Parameters:
    rfo (object): Redfish Client Login Object
    api (int): API Value
    unit (int): Unit Value

    Returns:
    list: JSON
    """
    res = rfo.get(f"/redfish/v{api}/systems/{unit}")
    if res.status != 200:
        print(f"Error: {res.status}: {res.read}")
        return "XXX"
    summary = ({**res.dict['ProcessorSummary'], **res.dict['Oem']['Hpe']['SystemUsage']})
    res = rfo.get(f"/redfish/v{api}/systems/{unit}/Processors/1")
    if res.status != 200:
        print(f"Error Proc 1: {res.status}: {res.read}")
        return "XXX"
    summary = ({**summary,
                **{'Manufacturer': res.dict['Manufacturer']},
                **{'InstructionSet': res.dict['InstructionSet']},
                **{'TotalCoresPerCPU': res.dict['TotalCores']},
                **{'TotalThreadsPerCPU': res.dict['TotalThreads']},
                })
    return json.dumps(summary)

