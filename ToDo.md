# ToDo

## Current task
Better Rocket Control, with the platform controller working it only needs to be refined 

## Control Rocket
<p>Currently a pain, ROS2 doesnt like floating joints or two joints in a row that would allow the 3D movement. Anther method would be creating a seperate transform and altering that. But how...?</p>
    Teleop?
    https://control.ros.org/master/doc/ros2_controllers/doc/controllers_index.html#available-controllers
    https://control.ros.org/master/doc/ros2_control_demos/example_4/doc/userdoc.html
    https://control.ros.org/master/doc/ros2_control_demos/example_1/doc/userdoc.html 

    http://wiki.ros.org/robot_mechanism_controllers/JointPositionController
    https://www.rosroboticslearning.com/ros-control


    https://www.youtube.com/watch?v=ZfVODpwVbS4


gazebo_msgs/EntityState
        

## Control Platform
Basic control provided by 'Cam_ctrl'. To make better by having it move faster the further the detected rocket is from the centre of the screen

## Impletment blob find: 
DONE! run:
```
ros2 run cv rocket_detect
```

https://www.youtube.com/watch?v=We6CQHhhOFo
https://answers.ros.org/question/361030/ros2-image-subscriber/

## Changing FOV on camera

Data?
https://www.reddit.com/r/ROS/comments/uvw8ij/multiple_robots_gazebo_ros2/

## Output of data
