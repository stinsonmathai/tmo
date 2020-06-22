import os
import json


def set_firmware(rfo, firmware, update_repo=True, update_target=False):
    """Upload firmware to iLO repository and optionally apply

    Parameters:
    rfo (object): Redfish session
    firmware (str): Path to file location (ie "data/ilo5_215.bin")
    update_repo (boolean): Upload firmware to iLO repository
    update_target (boolean): Apply firmware

    Returns:
    str: iLO response status
   """

    path = "/cgi-bin/uploadFile"
    body = []
    json_data = {'UpdateRepository': update_repo, 'UpdateTarget': update_target, 'ETag': 'atag', 'Section': 0}
    session_key = rfo.session_key

    filename = os.path.basename(firmware)
    with open(firmware, 'rb') as fle:
        output = fle.read()

    session_tuple = ('sessionKey', session_key)
    parameters_tuple = ('parameters', json.dumps(json_data))
    file_tuple = ('file', (filename, output, 'application/octet-stream'))

    body.append(session_tuple)
    body.append(parameters_tuple)
    body.append(file_tuple)
    header = {'Cookie': 'sessionKey=' + session_key}
    res = rfo.post(path, body, headers=header)
    #res = rfo.post(path, body=body, headers=header)
    if res.status != 200:
        print(f"HTTP Fail Status: {res.status} - {res.read}")
        return("XXX")
    return f"Success: {res.status} - {res.read}"

