Author: Leopold Klotz

Credit:
- learm_ros2, learm_ros2_description were initially created by Andrew Dassonville in his learm_ros2 package: https://github.com/andrewda/learm_ros2
- The learm_ros2_description package was modified by Leopold Klotz to correct and expand the URDF model of the robot arm
- The moveit configuration was created by Leopold Klotz using the moveit setup assistant

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


Connecting LeArm to WSL2 running Ubuntu and ROS2:
    - In a Powershell terminal, attach the usb: https://learn.microsoft.com/en-us/windows/wsl/connect-usb
        - usbipd list
        - usbipd bind --busid 2-10 # or whatever busid is listed, only needs to be done first time
        - usbipd attach --wsl --busid 2-10 # needs to be done every time you plug in or turn on arm
    - In a WSL2 terminal, ensure the proper udev rules are set: https://www.clearpathrobotics.com/assets/guides/kinetic/ros/Udev%20Rules.html
    - Should be accessable and connected within WSL2.



    