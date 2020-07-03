def set_profile(rfo, profile="GeneralPowerEfficientCompute", api=1, unit=1):
    """Set Workload Profile

    Parameters:
    rfo (object): Redfish session
    profile (str):  GeneralPowerEfficientCompute:General Power Efficient Compute
                    GeneralPeakFrequencyCompute:General Peak Frequency Compute
                    GeneralThroughputCompute:General Throughput Compute
                    Virtualization-PowerEfficient:Virtualization - Power Efficient
                    Virtualization-MaxPerformance:Virtualization - Max Performance
                    LowLatency:Low Latency
                    MissionCritical:Mission Critical
                    TransactionalApplicationProcessing:Transactional Application Processing
                    HighPerformanceCompute(HPC):High Performance Compute (HPC)
                    DecisionSupport:Decision Support
                    GraphicProcessing:Graphic Processing
                    I/OThroughput:I/O Throughput
                    Custom:Custom
    api (int): API version
    unit (int): Enumerated component unit

    Returns:
    str: iLO response status
    """

    body = {'Attributes': {'WorkloadProfile': profile}}
    res = rfo.patch(f"/redfish/v{api}/Systems/{unit}/bios/settings", body=body)
    if res.status != 200:
        print(f"HTTP Fail Status: {res.status} - {res.read}")
        return("XXX")
    return f"Success: {res.status} - {res.read}"

