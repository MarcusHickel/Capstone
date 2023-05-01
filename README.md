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

```
ros2 run robot_state_publisher robot_state_publisher --ros-args -p robot_description:="$(xacro path/to/my/xacro/file.urdf.xacro)"
```

syntax for launch files:
```
ros2 launch [packagename] [launcherfile]
```

3. Launch the Launch `joint_state_publisher_gui` with 
```
ros2 run joint_state_publisher_gui joint_state_publisher_gui
```

4. Launch Rvis
```
rviz2
```

- Set fixed frame to 'world'
- Add a 'RobotModel' display, with the topic set to '/robot_description', and alpha set to 0.8
- Add a 'TF' display with names enabled.