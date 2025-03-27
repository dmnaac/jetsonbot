import os
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument

def generate_launch_description():
    slam_params = {
        "use_sim_time": False
    }

    parameter_file = LaunchConfiguration('params_file')
    share_dir = get_package_share_directory('slam_pkg')
    params_declare = DeclareLaunchArgument('params_file',
                                           default_value=os.path.join(share_dir, 'config', 'slam.yaml'),
                                           description='Full path to the ROS2 parameters file to use for the slam_toolbox node')
    slam_cmd = Node(
        package="slam_toolbox",
        executable="sync_slam_toolbox_node",
        output='screen',
        parameters=[parameter_file, slam_params]
    )

    rviz_file = os.path.join(get_package_share_directory('slam_pkg'), 'config', 'slam.rviz')

    rviz_cmd = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        arguments=['-d',rviz_file]
    )

    ld = LaunchDescription()
    ld.add_action(params_declare)
    ld.add_action(slam_cmd)
    ld.add_action(rviz_cmd)

    return ld
