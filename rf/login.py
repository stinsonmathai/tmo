import redfish


def login(un, pw, url):
    """
    Login to Redfish API
    un: (str) User name
    pw: (str) User password
    url: (str) HTTPS RedFish API URL
    Return: Redfish object
    """
    try:
        rfo = redfish.RedfishClient(base_url=url, username=un, password=pw)
        rfo.login()
        return rfo

    except ServerDownOrUnreachableError as excp:
        raise Exception("ERROR: server not reachable or doesn't support RedFish.")
    except Exception as excp:
        raise excp

    #TODO: I logged in with the vpn turned on and then ran the getmodel and the prompt just hung