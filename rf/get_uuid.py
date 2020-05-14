def get_uuid(rfo, api=1, unit=1):
    """
        This function fetches the UUID of the server.
        URL is https://IP_ADDRESS/redfish/v1/systems/1/
        Information is in the following JSON snippet.
        "UUID":

            Parameters:
            object: Redfish Client Login Object
            int: API Value
            int: Unit Value

            Returns:
            string: UUID
        """
    res = rfo.get(f"/redfish/v{api}/systems/{unit}")
    if res.status != 200:
        print(f"Error: {res.status}: {res.read}")
        return "XXX"
    return res.dict['UUID']

