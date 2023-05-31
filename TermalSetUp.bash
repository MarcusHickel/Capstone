# To set up the termnials, I've got a funky monitor setup so might not work for all

gnome-terminal --geometry 127x24+150+1063 --title "Builder" --working-directory=/home/marcus/rockettrackingplatform/dev_ws -- bash -c "echo Building; source install/setup.bash; colcon build --symlink-install; exec bash -i"
gnome-terminal --geometry 127x24+150+1474 --title "Gazebo" --working-directory=/home/marcus/rockettrackingplatform/dev_ws -- bash -c "echo Sleeping for build 10s; sleep 10s; echo Launching Gazebo&Word; source install/setup.bash; ros2 launch trackingplatform test.launch.py; exec bash -i"
gnome-terminal --geometry 127x24+150+1885 --title "Detecter" --working-directory=/home/marcus/rockettrackingplatform/dev_ws -- bash -c "echo Sleeping for build 10s; sleep 10s; echo Launching Detecter; source install/setup.bash; ros2 run cv rocket_detect; exec bash -i"
gnome-terminal --geometry 127x24+150+2298 --title "Controller" --working-directory=/home/marcus/rockettrackingplatform/dev_ws -- bash -c "echo Sleeping for build 10s; sleep 10s; echo Launching Controller; source install/setup.bash; ros2 run cv cam_ctrl; exec bash -i"

gnome-terminal --geometry 127x24+150+1474 --title "Gazebo" --working-directory=/home/marcus/rockettrackingplatform/dev_ws -- bash -c "echo Sleeping for build 10s; echo Launching Gazebo&Word; source install/setup.bash; ros2 launch trackingplatform test.launch.py"

gnome-terminal --geometry 127x24+150+1885 --title "Detecter" --working-directory=/home/marcus/rockettrackingplatform/dev_ws -- bash -c "echo Sleeping for build 10s; echo Launching Detecter; source install/setup.bash; ros2 run cv rocket_detect"

gnome-terminal --geometry 127x24+150+2298 --title "Controller" --working-directory=/home/marcus/rockettrackingplatform/dev_ws -- bash -c "echo Sleeping for build 10s; echo Launching Controller; source install/setup.bash; ros2 run cv cam_ctrl"

