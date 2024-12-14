# Setting Up Your Motor

Before we can begin commanding your motor through C++, there are a few steps that must be followed first.

## Setting Up Hardware and Testing Your Motor

Before continuing onto any software development, make sure that you have read through and followed the steps in the Orca Series Quickstart Guide, which can be found on [our downloads page](https://irisdynamics.com/downloads). We recommend testing your motors functionality through IrisControls, also hosted on our downloads page, before beginning to operate your motor through the SDK.

### Windows

Windows users will need to update a setting on their RS422 cable. Each cable has a built in latency of 16ms by default. For the RS485 cable, this is fine, but the SDK requires that this latency setting is reduced as much as possible. This allows for high speed communication with your motor. To update this setting, follow these steps:
 - Ensure your cables are connected to your computer
 - Open Device Manager
 - Navigate to "Ports (COM & LPT)" and expand the dropdown menu
 - Right click on the COM port for your RS422 cable and select "Properties"
    - If you do not know which COM port number corresponds to your RS422 cable, try unplugging and plugging back in your cable. The COM port you're looking for should disappear and reappear in the dropdown options
 - Under the "Port Settings" tab of the properties window, select "Advanced"
 - Set the "Latency Timer (msec)" option to a value of 1
 - Select Ok to confirm your selections

Keep a note of what the COM port number for your RS422 cable is. You will need it for each time you want to connect to your motor through the SDK.

## Building the SDK

If you have not downloaded and built the SDK yet, navigate to [our Github repo for the SDK](https://github.com/IrisDynamics/orcaSDK) and follow the build/install instructions in the README.

## 

Once you've completed everything listed above, you're ready to begin coding! Walk through [the first tutorial](../01_HelloWorld_ReadPosition/01_HelloWorld_ReadPosition.md) to learn how to set up a basic project using our SDK.