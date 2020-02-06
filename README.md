# Tutorials for the Robotont platform

## Table of Contents
1. [Control your Robotont using an Android device](#how-to-control-your-robotont-using-an-android-device)

## How to control your Robotont using an Android device
**Description:** This tutorial will walk you through how to control your Robotont from an Android phone or tablet.

### 1. Download the control app from the Google Play Store. 
* From your Android device, go to Google Play Store and install the [ROS Control](https://play.google.com/store/apps/details?id=com.robotca.ControlApp&hl=en) app.
### 2. Wifi setup
* Connect your Android device to the Robotont's hotspot or the same network the Robotont is connected to.
### 3. Prepare the Robotont
* Make sure that you have followed the Robotont bring up tutorials and installed the packages as documented in the tutorial.
* SSH to Robotont.
* From `robotont_driver` package, launch the basic driver launch file:<br/>
``` roslaunch robotont_driver driver_basic.launch ```

### 4. Connecting your phone to Robotont
* Open the ROS Control app on your phone.
* Add a new robot using the plus sign in the top right corner and give it a desired name.
* Insert the Robotont IP into Master URI field by entering the following:<br/>
``` http://Robotont_IP:11311 ```
* Click on "Show advanced options" in the prompted window and fill in "Joystick" and "Odometry" topic names with "robotont/cmd_vel" and "robotont/odom", respectively.
* Click OK to add the robot.
* Now you can select the robot from the list and teleoperate it using the touch joystick button.
