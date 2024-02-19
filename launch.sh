#!/bin/bash

# Change directory into the package
cd ~/learm_ws

# Source ROS
source /opt/ros/humble/setup.bash

# Build the package
colcon build

# Source the package
source ~/learm_ws/install/setup.bash

# Launch the package
ros2 launch learm_ros2 run.launch.py