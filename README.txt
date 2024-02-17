Author: Leopold Klotz

Credit:
- learm_ros2, learm_ros2_description, and learm_ros2_moveit_config packages were all taken from Andrew Dassonville's learm_ros2 repository.
- The learm_ros2 repository was used as a starting point for this project but has been modified and expanded upon.

To build the project:
    - cd learm_ws
    - source /opt/ros/humble/setup.bash
    - colcon build

To run RVIZ with the model:
# What this does:
# 1. Launches RVIZ2 (with the config from learm_ros2_description)
# 2. Launches the joint state publisher (urdf from learm_ros2_description)
# 3. Launches the robot state publisher (urdf from learm_ros2_description)
    - cd learm_ws
    - source /opt/ros/humble/setup.bash
    - source install/setup.bash
    - ros2 launch learm_ros2 run.launch.py

To run the follower node:
# What this does:
# 1. Launches the follower node (from learm_ros2)
# 2. The follower node listens to the /joint_states topic and controls the appropriate servos to follow the joint states
    - cd learm_ws
    - source /opt/ros/humble/setup.bash
    - source install/setup.bash
    - ros2 run learm_ros2 follower.launch.py

    