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

2. Launch the listener or talker launcher to test, next the robot state publisher
```
ros2 launch trackingplatform talker.launch.py
```
Manually running robot state publisher, not needed once launch file is working correctly
```
ros2 run robot_state_publisher robot_state_publisher --ros-args -p robot_description:="$(xacro path/to/my/xacro/file.urdf.xacro)"
```

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

3. Launch the `joint_state_publisher_gui` with
```
ros2 run joint_state_publisher_gui joint_state_publisher_gui
```

4. Launch Rvis
```
rviz2
```

5. Control the Camera platform
```
ros2 topic pub /forward_position_controller/commands std_msgs/msg/Float64MultiArray "data:
- 1
- 1"
```

- Set fixed frame to 'world'
- Add a 'RobotModel' display, with the topic set to '/robot_description', and alpha set to 0.8
- Add a 'TF' display with names enabled.

ToDo
Control Rocket
    Teleop?
    https://control.ros.org/master/doc/ros2_controllers/doc/controllers_index.html#available-controllers
    https://control.ros.org/master/doc/ros2_control_demos/example_4/doc/userdoc.html
    https://control.ros.org/master/doc/ros2_control_demos/example_1/doc/userdoc.html 



    http://wiki.ros.org/robot_mechanism_controllers/JointPositionController
    https://www.rosroboticslearning.com/ros-control


        Current issue: 
        None

        Controller mananger wasnt spawning 
        running ctrl.launch.py 
        [gzserver-1] [WARN] [1683695189.182994074] [gazebo_ros2_control]: There is no joint or sensor available
        [gzserver-1] [FATAL] [1683695189.183028701] [gazebo_ros2_control]: Could not initialize robot simulation interface
        Fixed? Not sure what is issue was, just started working


        controller.yaml is failing. 
        Fixed: config folder added to cmake 

    Launch File
    Controllers yaml
    URDF file
        Description
        ros2_control tag
    RViz config
    Test nodes

Control Platform
Impletment blob find
Changing FOV on camera

Issues:
Running joint state publisher gui breaks rviz ability to see camera and doesnt control gazebo
TF_OLD_DATA