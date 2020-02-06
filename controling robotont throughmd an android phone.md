# How to control your robotont using an Android device
**Description:** This tutorial will walk you through how to control your Robotont from an Android phone or tablet.
### 1. Wifi setup
* Connect you android device to the Robotont's hotspot or the same network the Robotont is connected to.
### 2. Prepare the Robotont
* Make sure that you have follwowed the robotont bring up tutorials and install the packages as documented in the tutorial.
* SSH to Robotont
* From robotont_driver package, launch the basic driver laucnh file. <br/>

``` roslaunch robotont_driver driver_basic.launch ```

### 3. Download the control app from the Google Play Store. 
* From your android device, go Google Play Store and install the [ROS Control](https://play.google.com/store/apps/details?id=com.robotca.ControlApp&hl=en) app.
### 4. Connecting your phone to Robotont
* Open the ROS Control app on your phone.
* Add a new robot using the plus sign in the top right corner and give it a desired name.
* Insert the Robotont IP into Master URI field like the following: <br/>

``` http://Robotont_IP:11311 ```

* Click on show advanced options in the prompted window and fill in Joystick and Odometry topic names with "robotont/cmd_vel" and "robotont/odom", respectively.
* Click on OK to add te robot.
* Now, you can select the robot from the list and teleoperate it using the touch joystick.
