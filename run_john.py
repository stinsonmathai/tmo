import rf
from rf.config import *


# Login session
rfo = rf.login(un, pw, url)

# Functions
print(rf.create_user(rfo, username, password, role))


"""
api=1
unit=1
print(rf.enable_sriov(rfo))
print(rf.reboot_server(rfo))
print(rf.set_hostname(rfo, hostname="host.domain.com"))
print(rf.set_dns(rfo, dns="8.8.8.8"))
print(rf.set_timezone(rfo, tz="UtcM5"))
print(rf.set_license_key(rfo, key="xxxx"))
print(rf.set_power_options(rfo, mode="BalancedMode"))
print(rf.set_ntp(rfo, ntp=["132.163.96.5", "128.138.141.177"]))
print(rf.set_firmware(rfo, 'data/ilo5_215.bin', True, False))
print(rf.set_snmp(rfo, destination=["10.0.1.100"]))
print(rf.set_snmp_alerts(rfo, alert=True, communities=["public", "", ""]))
"""


# Logoff
rfo.logout()
