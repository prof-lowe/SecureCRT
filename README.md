# SecureCRT Scripts and Settings
Repository of scripts and settings I use for SecureCRT

## Keyword Highlights
The josh.ini file contains the Keyword Highlight settings I use in SecureCRT to get certain words to highlight in particular colors. It's designed specifically to work on the console of Cisco devices, so the highlights might not make sense if you apply them to non-Cisco devices.

In SecureCRT session settings, I have my window appearance set to "Traditional" color scheme (black background, light grey font). The keyword highlights might not look right if you're using a different color scheme.
Also, ensure that the "Highlight Style" setting is set to "Color" and the "Match Style" settings is set to "Whole words".

## Scripts
### ClearDevice
This script can be run from within SecureCRT to erase a device (router or switch). It will erase the startup configuration, delete the vlan.dat file if it exists, and reload the device. Note that you must be in privileged EXEC mode (type "enable") for the script to work. If you are in configuration mode, the script will use Ctrl-C to exit config mode first, before clearing the device

### ExportConfig
This script can be run from within SecureCRT to capture the output of the command `show run brief`. When run, the script will prompt you for a location where you want to save the file. It then captures the running configuration of the device and saves it to your selected location. The name of the file will be `<tabname>.txt`, where `<tabname>` is the name of the SecureCRT tab that was active at the time you ran the script. If you want your file names to be useful, be sure to name your tabs appropriately (e.g., R1, R2, R3, etc.)
