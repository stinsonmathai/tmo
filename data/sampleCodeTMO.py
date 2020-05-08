def get_model(un, pw, ip):
    url = 'https://' + ip + '/redfish/v1/Systems/System.Embedded.1'
    payload = ""
    headers = {'content-type': 'application/json'}
    try:
        response = requests.request(
            "GET", url, data=payload, headers=headers, verify=False, auth=(un, pw), timeout=2)
    except:
        return 'pwd or connect err'
    else:
        if response.status_code != 200:
            print("\n- Bios FAIL, GET command failed to get Dell switch connection collection, st
            atus
            code % s
            " %
            (response.status_code))
            return 'XXX'
        content = json.loads(response.text)
        output = content["Model"]
        return str(output)


def get_firmware(un, pw, ip):
    url = 'https://' + ip + '/redfish/v1/Managers/iDRAC.Embedded.1'
    payload = ""
    headers = {'content-type': 'application/json'}
    try:
        response = requests.request(
            "GET", url, data=payload, headers=headers, verify=False, auth=(un, pw), timeout=2)
    except:
        return 'pwd or connect err'
    else:
        if response.status_code != 200:
            print("\n- Bios FAIL, GET command failed to get Dell switch connection collection, st
            atus
            code % s
            " %
            (response.status_code))
            return "pwd or connect err"
        content = json.loads(response.text)
        output = content["FirmwareVersion"]
        return str(output)


def get_memory_count(un, pw, ip):
    url = 'https://' + ip + '/redfish/v1/Systems/System.Embedded.1/Memory'
    payload = ""
    headers = {'content-type': 'application/json'}
    try:
        response = requests.request(
            "GET", url, data=payload, headers=headers, verify=False, auth=(un, pw), timeout=2)
    except:
        return 'pwd or connect err'
    else:
        if response.status_code != 200:
            print("\n- Bios FAIL, GET command failed to get Dell switch connection collection, status code %s" %
                  (response.status_code))
            return 'XXX'
        content = json.loads(response.text)
        output = len(content["Members"])
        return str(output)