import rf
from rf.config import *

# Login session
rfo = rf.login(un, pw, url)

# Functions
print(rf.get_model(rfo))

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

print(rf.set_hostname(rfo, hostname="host.domain.com"))
print(rf.enable_sriov(rfo))
print(rf.reboot_server(rfo))
"""

# Logoff
rfo.logout()
