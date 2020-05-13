def set_boot_order(rfo, order, api=1, unit=1):
    """Set processor turbo boost technology

    Parameters:
    rfo (object): Redfish login session
    order (list): Ordered list of devices
    api (int): API version
    unit (int): Enumerated component unit

    Returns:
    str: iLO response status
    """
    body = {'DefaultBootOrder': order}
    res = rfo.patch(f"/redfish/v{api}/Systems/{unit}/bios/boot/settings", body)
    if res.status != 200:
        print(f"HTTP Fail Status: {res.status} - {res.read}")
        return "XXX"
    return f"Success: {res.status} - {res.read}"
