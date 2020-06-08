# Unattended ESXi Installation

### Install HTTP server

HTTP web server will be used to host the custom ISO as well as the kickstart file.  

### Download HPE Customized ESXi Image

HPE customized ESXi images include all of the required drivers and management software to run ESXi on HPE servers, and works seamlessly with Intelligent Provisioning.

* https://www.hpe.com/us/en/servers/hpe-esxi.html

### Modify ESXi ISO

* Modify ISO /BOOT.CFG and /EFI/BOOT/BOOT.CFG.  Both files will be identical
    * kernelopt=runweasel ks=http://IP/ks.cfg
    
### Create Kickstart configuration

Sample ks.cfg file hosted on HTTP server:

    vmaccepteula
    rootpw chAngme0!
    install --firstdisk=local --overwritevmfs --novmfsondisk
    network --bootproto=static --device=vmnic0 --ip=16.83.130.28 --netmask=255.255.254.0 --gateway=16.83.130.1 --nameserver=8.8.8.8 --hostname=tmoserver
    reboot --noeject
    %firstboot --interpreter=busybox
    vim-cmd hostsvc/enable_ssh
    vim-cmd hostsvc/start_ssh
    esxcli system maintenanceMode set -e true
    reboot
    
### Install ESXi via Redfish

Insert virtual media and reset server:

    rf.install_os(rfo, "http://16.214.16.78/custom.iso")
  


