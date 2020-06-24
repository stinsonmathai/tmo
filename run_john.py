import rf
from rf.config import *

# Login session
rfo = rf.login(un, pw, url)



print(rf.set_ilo_dhcp(rfo, dhcp=False))

ip = {"IPv4Addresses": [{"Address": "16.91.158.182", "Gateway": "16.91.152.1", "SubnetMask": "255.255.248.0"}]}
print(rf.set_ilo_ip(rfo, ip=ip))

dns = ["16.110.135.52", "16.110.135.51"]
print(rf.set_ilo_dns(rfo, dns=dns))

print(rf.get_ilo_net_blob(rfo))


print(rf.get_sriov(rfo))

print(rf.get_timezone(rfo))
print(rf.set_timezone(rfo, tz="UtcM5"))

print(rf.get_snmp_alerts(rfo))
print(rf.set_snmp_alerts(rfo, alert=True, communities=["public", "", ""]))

print(rf.get_snmp(rfo))
print(rf.set_snmp(rfo, destinations=["10.0.1.100"]))

print(rf.get_power_options(rfo))
print(rf.set_power_options(rfo, mode="BalancedMode"))

print(rf.get_ntp(rfo))
# TODO (DHCP ENABLED?)
print(rf.set_ntp(rfo, ntp=["132.163.96.5", "128.138.141.177"]))

print(rf.get_firmware(rfo))
print(rf.set_firmware(rfo, 'data/ilo5_215.bin', True, False))

print(rf.get_boot_order(rfo))
print(rf.set_boot_order(rfo, order=["Cd", "Usb", "EmbeddedStorage", "PcieSlotStorage", "EmbeddedFlexLOM",
                                    "PcieSlotNic", "UefiShell"]))

print(rf.get_turbo(rfo))
print(rf.set_turbo(rfo, mode="Enabled"))

print(rf.get_jitter(rfo))
print(rf.set_jitter(rfo, mode="Auto-tuned"))

print(rf.get_virtualization(rfo))
print(rf.set_virtualization(rfo, mode="Enabled"))

# print(rf.get_dns(rfo))
# print(rf.set_dns(rfo, dns="16.110.135.52"))

# print(rf.get_hostname(rfo))
# print(rf.set_hostname(rfo, "tmo"))

# print(rf.install_os(rfo, "http://16.116.132.70/custom2.iso"))

print(rf.reboot_server(rfo))







'''
print(rf.get_model(rfo))
print(rf.get_firmware(rfo))
print(rf.get_memory_total(rfo))
print(rf.get_tag(rfo))
print(rf.get_bios(rfo))
print(rf.get_cpu(rfo))
print(rf.get_status(rfo))
print(rf.get_uuid(rfo))
print(rf.get_disk_capacity(rfo))
print(rf.get_disk_count(rfo))
print(rf.get_disk_blob(rfo))
print(rf.get_nic_blob(rfo))
print(rf.get_cpu_blob(rfo))
print(rf.get_mem_blob(rfo))
print(rf.get_nic_names(rfo))


print(rf.set_dns(rfo, dns="8.8.8.8"))
print(rf.set_timezone(rfo, tz="UtcM5"))
print(rf.set_license_key(rfo, key="xxxx"))
print(rf.set_power_options(rfo, mode="BalancedMode"))
print(rf.set_ntp(rfo, ntp=["132.163.96.5", "128.138.141.177"]))
print(rf.set_firmware(rfo, 'data/ilo5_215.bin', True, False))
print(rf.set_snmp(rfo, destination=["10.0.1.100"]))
print(rf.set_snmp_alerts(rfo, alert=True, communities=["public", "", ""]))
print(rf.create_user(rfo, "abc123", "ef2#adAD.", "Administrator"))
print(rf.change_password(rfo, "abc123", "ef2#adAD."))
print(rf.set_jitter(rfo, mode="Auto-tuned"))
print(rf.set_turbo(rfo, mode="Enabled"))
print(rf.set_virtualization(rfo, mode="Enabled"))
print(rf.set_boot_order(rfo, order=["Cd", "EmbeddedStorage", "PcieSlotStorage", "EmbeddedFlexLOM",
                                    "PcieSlotNic", "UefiShell", "Usb"]))
print(rf.install_os(rfo, "http://16.214.16.78/custom.iso"))
print(rf.create_virtual_disks(rfo))
'''

# Logoff
rfo.logout()
