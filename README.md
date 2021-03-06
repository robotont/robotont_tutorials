# Tutorials for the robotont platform

## Table of Contents
1. [Control your robotont using an Android device](#how-to-control-your-robotont-using-an-android-device)

## How to control your robotont using an Android device
**Description:** This tutorial will walk you through how to control your robotont from an Android phone or tablet.

### 1. Download the control app from the Google Play Store. 
* From your Android device, go to Google Play Store and install the [ROS Control](https://play.google.com/store/apps/details?id=com.robotca.ControlApp&hl=en) app.
### 2. WiFi setup
* Connect your Android device to the robotont's hotspot or the same network the robotont is connected to.
### 3. Prepare the robotont
* In order to start working with robotont, start its ROS driver on the on-board computer.
* Create an SSH-connection to your robotont (find the username, IP address, and password in your robotont's user guide):<br/>
``` ssh username@robotont_IP_address ```
* From `robotont_driver` package, launch the basic driver launch file:<br/>
``` roslaunch robotont_driver driver_basic.launch ```

### 4. Connecting your phone to robotont
* Open the ROS Control app on your phone.
* Add a new robot using the plus sign in the top right corner and give it a desired name.
* Insert the robotont's IP address into Master URI field by entering the following:<br/>
``` http://robotont_IP_address:11311 ```
* Click on "Show advanced options" in the prompted window and fill in "Joystick" and "Odometry" topic names with "robotont/cmd_vel" and "robotont/odom", respectively.
* Click OK to add the robot.
* Now you can select the robot from the list and teleoperate it using the touch joystick button.
