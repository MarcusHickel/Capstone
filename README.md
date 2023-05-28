# Capstone
This is my Capstone. I am building a simulation to model the speed of which cameras would need to move to track a low powered model rocket in flight

How to run
1. Build the package with colcon
```
cd ~/dev_ws
colcon build --symlink-install 
```
(--symlink-install uses symlink instead of copies so rebuilding isnt nesscary when tweaking files)

Source the workspace in dev_ws
```
source install/setup.bash
```

2. Launch the following in seperate terminals
```
ros2 launch trackingplatform test.launch.py

ros2 run cv rocket_detect

ros2 run cv cam_ctrl
```
### note that the gazebo client has trouble showing the rocket, but it appears fine in the camera topic.


syntax for launch files:
```
ros2 launch [packagename] [launcherfile]
```
Available launch files
```
ctrl.launch.py -- Controller launcher, Launches the Camera platform and Gazebo with the forward_position_controler
listener.launch.py  -- Launches the listener script, used with talker.launch.py to debug
rs.launch.py -- Rocket, Spawns the rocket
rsp.launch.py -- Robot state publisher
sim.launch.py -- Launches the camera platform in Simulation (Gazebo) 
talker.launch.py -- Talker script used with listern script for debugging
```

# Notes

Launch ctrl first then rs
note: if two camera platforms spawn, delete the second and relaunch rs.launch.py

Launch the `joint_state_publisher_gui` with (Doesnt work, the camera is controled on a different topic)
```
ros2 run joint_state_publisher_gui joint_state_publisher_gui
```

Launch Rvis
```
rviz2
```

Manually Control the Camera platform
```
ros2 topic pub /forward_position_controller/commands std_msgs/msg/Float64MultiArray "data:
- Altitude(FLOAT)
- Azimuth(FLOAT)"
```
Manually running robot state publisher, not needed once launch file is working correctly
```
ros2 run robot_state_publisher robot_state_publisher --ros-args -p robot_description:="$(xacro path/to/my/xacro/file.urdf.xacro)"
```


ros2 topic list -t
ros2 control list_hardware_interfaces

rqt
rqt_graph


```
Distributor ID:	Ubuntu
Description:	Ubuntu 20.04.6 LTS
Release:	20.04
Codename:	focal

Gazebo 11.11.0
ROS2 FOxy
```