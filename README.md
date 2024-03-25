# SecureCRT Scripts and Settings
Repository of scripts and settings I use for SecureCRT

## Keyword Highlights
The josh.ini file contains the Keyword Highlight settings I use in SecureCRT to get certain words to highlight in particular colors. It's designed specifically to work on the console of Cisco devices, so the highlights might not make sense if you apply them to non-Cisco devices.

In SecureCRT session settings, I have my window appearance set to "Traditional" color scheme (black background, light grey font). The keyword highlights might not look right if you're using a different color scheme.
Also, ensure that the "Highlight Style" setting is set to "Color" and the "Match Style" settings is set to "Whole words".

### Usage
To add the Keyword Highlights in SecureCRT, first download the .ini file and save it in the Keywords folder in your SecureCRT Settings folder. If you're not sure where your SecureCRT settings are stored, in SecureCRT open the **Options** menu and choose **Global Options...**. Under the **General** menu item, select **Configuration Paths** to see the location of your SecureCRT settings.

Once you've saved the .ini file in the appropriate folder, you can go to **Options** > **Edit Default Session...** then under **Terminal** choose **Keyword Highlighting** to see the appropriate settings. From the **List name** dropdown menu at the top of the screen, chose the .ini file that you just downloaded, and click **OK**. If you already have saved sessions in SecureCRT, you might be prompted to apply the Keyword Highlights to those saved sessions as well.

## Scripts
### ClearDevice
This script can be run from within SecureCRT to erase a device (router or switch). It will erase the startup configuration, delete the vlan.dat file if it exists, and reload the device. Note that you must be in privileged EXEC mode (type "enable") for the script to work. If you are in configuration mode, the script will use Ctrl-C to exit config mode first, before clearing the device

### ExportConfig
This script can be run from within SecureCRT to capture the output of the command `show run brief`. When run, the script will prompt you for a location where you want to save the file. It then captures the running configuration of the device and saves it to your selected location. The name of the file will be `<tabname>.txt`, where `<tabname>` is the name of the SecureCRT tab that was active at the time you ran the script. If you want your file names to be useful, be sure to name your tabs appropriately (e.g., R1, R2, R3, etc.)

### Usage
SecureCRT scripts can technically be saved anywhere on your computer, although having a dedicated folder for them is probably best. To run either of the scripts you can choose **Script** > **Run...** and select the script from the location where you saved it. 

Personally, I have found that these two scripts are very useful as SecureCRT buttons, which allow you to run them with a single click. To set up button, first make sure the button bar is visible by clicking the **View** menu and ensuring that **Button Bar** has a check next to it. To add a new button, right-click on the button bar and choose **New Button...**. For the **Action Function** dropdown, choose **Run Script** and in the field beside that, choose the script you want the button to run (use the **...** button at the end of the field to search for the script). Neither script requires any arguments. Label the button and and choose an icon colour as you like, then click **OK** to create the button.
