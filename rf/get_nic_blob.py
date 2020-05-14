import json


def get_nic_blob(rfo, api=1, unit=1):
    """
        This function fetches information about EACH of the network interfaces of the server.
        URL is https://IP_ADDRESS/redfish/v1/systems/1/EthernetInterfaces/

        NOTE: There could be multiple interfaces in the server.

            Parameters:
            object: Redfish Client Login Object
            int: API Value
            int: Unit Value

            Returns:
            JSON Array: Details of each of the Ethernet Interfaces in the Server
    """
    blob = []
    res = rfo.get(f"/redfish/v{api}/systems/{unit}/EthernetInterfaces")
    if res.status != 200:
        print(f"Error: {res.status}: {res.read}")
        return "XXX"
    members = res.dict['Members']
    for m in members:
        res = rfo.get(m['@odata.id'])
        if res.status != 200:
            print(f"Member Error: {res.status}: {res.read}")
            return "XXX"  #TODO should we break out here or just punch through the rest and note the error?
        blob.append(res.dict)
        #blob = blob + str(res.dict) #TODO -- this maynot be needed
    blob_json = json.dumps(blob)
    # This will return a JSON Array which has all the values for each of the Interfaces, Best Viewed in a JSON Viewer
    return blob_json
