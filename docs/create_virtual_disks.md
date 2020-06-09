# Create Virtual RAID Disk

### Notes

* Although a request to create a virtual RAID disk may be successful, there are multiple reasons why it could fail.  Any error messages after system reset will be listed here:  https://16.83.131.155/redfish/v1/systems/1/smartstorageconfig1
* Pending settings are stored here:  https://IP/redfish/v1/systems/1/smartstorageconfig1/settings
* You can view the configured disk in multiple places: 
    * https://16.83.131.155/redfish/v1/systems/1/smartstorage/arraycontrollers/12/LogicalDrives/1
    * https://16.83.131.155/redfish/v1/systems/1/smartstorageconfig1
    * https://16.83.131.155/redfish/v1/systems/1/smartstorageconfig1/settings
    
### Create RAID Disk

By default, a default RAID1 configuration is hard coded in the create_virtual_disks.py function:

    raid = {
        "DataGuard": "Disabled",
        "LogicalDrives": [
           {
              "CapacityGiB": 275,
              "Raid": "Raid1",
              "LogicalDriveName": "MyLD",
              "DataDrives": [
                    "1I:1:1",
                    "1I:1:2"
              ],
              # "Accelerator": "ControllerCache" # Requires redundant power
           }
        ]
    }

If a raid dictionary variable is passed to the function, it will be used instead of the above.
    
To create the virtual raid disk:

    print(rf.create_virtual_disks(rfo))

Or with the raid variable passed to the function containing the raid configuration:

    print(rf.create_virtual_disks(rfo, raid)) 




