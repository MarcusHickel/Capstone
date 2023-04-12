# Capstone
This is my Capstone. I am building a simulation to model the speed of which cameras would need to move to track a low powered model rocket in flight

How to run
1. Build the package with colcon
```
cd ~/dev_ws
colcon build --symlink-install 
```
(--symlink-install uses symlink instead of copies so rebuilding isnt nesscary when tweaking files)
2. Launch the listener or talker launcher with <- To replace with robot state publisher>
```
ros2 launch trackingplatform talker.launch.py
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

- Set fuxed fran to 'world'
- Add a 'RobotModel' display, with the topic set to '/robot_description', and alpha set to 0.8
- Add a 'TF' display with names enabled.