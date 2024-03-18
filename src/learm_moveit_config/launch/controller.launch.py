import launch
from launch import LaunchDescription
from launch_ros.actions import Node
import os
import xacro
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():

    urdf_path_xacro = os.path.join(
        get_package_share_directory('learm_moveit_config'),
        'config/learm.urdf.xacro')
    robot_desc = xacro.process_file(urdf_path_xacro).toxml()

    

    # Launch the controller manager node
    controller_manager_node = Node(
        package='controller_manager',
        executable='ros2_control_node',
        name='ros2_control_node',
        namespace='',
        output='screen',
        parameters=[
            {'use_sim_time': False},  # Set to True if using simulated time
            {'ros__parameters': {'robot_description': robot_desc}},  # Path to your robot description file
            {'robot_hardware': 'file:///path/to/your/hardware_config.yaml'},  # Path to your hardware configuration file
            {'controller_manager': 'file:///path/to/your/controllers.yaml'}  # Path to your controllers configuration file
        ]
    )

    return LaunchDescription([controller_manager_node])

if __name__ == '__main__':
    generate_launch_description()
