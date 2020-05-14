
import rf
from rf.config import *


# This is Stinson's run file for testing


# Login session
rfo = rf.login(un, pw, url)
k = rf.get_nic_blob(rfo)
help(rf.get_nic_blob)


# Logoff
rfo.logout()



#finished by Stin
"""print(rf.get_model(rfo))
print(rf.get_firmware(rfo))
print(rf.get_memory_total(rfo))
print(rf.get_tag(rfo))
"""





"""
# Completed functions
print(rf.get_model(rfo))
print(rf.get_uuid(rfo))
print(rf.get_nic_blob(rfo))
print(rf.get_nic_blob(rfo))
print(rf.get_network_adapters_blob(rfo))
print(rf.get_firmware(rfo))
print(rf.get_memory_total(rfo))
print(rf.get_disk_count(rfo))
print(rf.get_disk_capacity(rfo))
print(rf.get_disk_blob(rfo))

print(rf.enable_sriov(rfo))
print(rf.reboot_server(rfo))
print(rf.set_hostname(rfo, hostname="host.domain.com"))
print(rf.set_dns(rfo, dns="8.8.8.8"))
print(rf.set_timezone(rfo, tz="UtcM5"))
print(rf.set_license_key(rfo, key="xxxx"))
print(rf.set_power_options(rfo, mode="BalancedMode"))
"""

'''f"Ethernet Interface {m['@odata.id']} MAC Address: {res.dict['MACAddress']}\n"
f"Ethernet Interface {m['@odata.id']} IP4 Addresses: {res.dict['IPv4Addresses']}\n"
f"Ethernet Interface {m['@odata.id']} Name: {res.dict['Name']}\n"
f"Ethernet Interface {m['@odata.id']} Interface Enabled: {res.dict['InterfaceEnabled']}\n"
f"Ethernet Interface {m['@odata.id']} Link Status: {res.dict['LinkStatus']}\n"
f"Ethernet Interface {m['@odata.id']} Link State: {res.dict['Status']['State']}\n"
f"Ethernet Interface {m['@odata.id']} Link Health: {res.dict['Status']['Health']}\n"
f"Ethernet Interface {m['@odata.id']} Name Servers: {res.dict['NameServers']}\n"
f"Ethernet Interface {m['@odata.id']} Speed Mbps: {res.dict['SpeedMbps']}\n"
'''

'''
def get_all_values(res_dict):
    for key, value in res_dict.items():
        if type(value) is dict:
            get_all_values(value)
        else:
            print(key, ":", value)


get_all_values(res_dict)'''