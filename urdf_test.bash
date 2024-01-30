#!/bin/bash

source /opt/ros/humble/setup.bash &
cd ~/learm_ws/src/urdf_example &
colcon build & 

# Spawn first terminal and run command
gnome-terminal --tab --title="Terminal 1" -- bash -c "ros2 launch urdf_example rsp.launch.py; exec bash"

# Spawn second terminal and run command
gnome-terminal --tab --title="Terminal 2" -- bash -c "ros2 run joint_state_publisher_gui; exec bash"

# Run the third command in the current terminal
rviz2 &
