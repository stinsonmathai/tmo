import rf
from rf.config import *

# Login session
rfo = rf.login(un, pw, url)

print(rf.set_dns(rfo, dns="8.8.8.8"))


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
