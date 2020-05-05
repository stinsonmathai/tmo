import rf

un = "admin"
pw = "admin"
url = "https://16.91.158.182"
api = 1
unit = 1

rf.get_nic_blob(un, pw, url)
rf.get_nic_ilo_blob(un, pw, url)
rf.get_network_adapters_blob(un, pw, url)
rf.get_model(un, pw, url)
rf.get_firmware(un, pw, url)
rf.get_memory_total(un, pw, url)
rf.get_disk_count(un, pw, url)
rf.get_disk_capacity(un, pw, url)
rf.get_disk_blob(un, pw, url)
rf.get_uuid(un, pw, url)

rf.reboot_server(un, pw, url)
rf.set_hostname(un, pw, url, hostname="host.domain.com")
rf.enable_sriov(un, pw, url)


# this is a test