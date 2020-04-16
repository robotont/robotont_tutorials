# Tutorials for the robotont platform

## Table of Contents
1. [Control your robotont using an Android device](#how-to-control-your-robotont-using-an-android-device)

2. [AR tracking based follow the leader demo](#follow-the-leader-demo-with-ar-tags)

3. [Use python to send velocity commands to robotont](#use-python-to-send-velocity-commands-to-robotont)

3. [RTabMap 3D mapping on robotont](#3d-mapping)

4. [2D SLAM (Simultaneous Localisation and Mapping)](#2d-slam)

## How to control your robotont using an Android device
**Description:** This tutorial will walk you through how to control your robotont from an Android phone or tablet.

### 1. Download the control app from the Google Play Store. 
* From your Android device, go to Google Play Store and install the [ROS Control](https://play.google.com/store/apps/details?id=com.robotca.ControlApp&hl=en) app.
### 2. WiFi setup
* Connect your Android device to the robotont's hotspot or the same network the robotont is connected to.
### 3. Prepare the robotont
* In order to start working with robotont, start its ROS driver on the on-board computer.
* Create an SSH-connection to your robotont (find the username, IP address, and password in your robotont's user guide):<br/>

```bash
ssh username@robotont_IP_address
```

* From `robotont_driver` package, launch the basic driver launch file:<br/>
```bash
roslaunch robotont_driver driver_basic.launch
```

### 4. Connecting your phone to robotont
* Open the ROS Control app on your phone.
* Add a new robot using the plus sign in the top right corner and give it a desired name.
* Insert the robotont's IP address into Master URI field by entering the following:<br/>
```bash
http://robotont_IP_address:11311
```
* Click on "Show advanced options" in the prompted window and fill in "Joystick" and "Odometry" topic names with "robotont/cmd\_vel" and "robotont/odom", respectively.
* Click OK to add the robot.
* Now you can select the robot from the list and teleoperate it using the touch joystick button.

## Follow the leader demo with AR tags

### 1. Prerequisites
* Install ar\_track\_alvar ROS package

### 2. Using the demo
* Start the tracking and control nodes

```bash
roslaunch robotont_tutorials ar_follow_the_leader.launch
```


## Use python to send velocity commands to robotont

### 1. Make sure robotont driver is running.
TODO: Ref to a separate section that covers starting/checking the service or running driver node manually.
### 2. Run the python script
```bash
rosrun robotont_tutorials robotont_move.py
```

## 3D mapping
TODO:

```bash
roslaunch robotont_tutorials 3d_mapping.launch
```

## 2D SLAM
TODO: 

```bash
roslaunch robotont_tutorials 2d_slam.launch
```
