import os
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():

    map_name = 'map_1744085681.yaml'
    map_root = '/home/tmrobot/jetsonbot/SLAM/map/nav/'

    map_file = os.path.join(
        map_root,
        map_name
    )
    
    nav_param_file = os.path.join(
        get_package_share_directory('nav2_pkg'),
        'config',
        'nav2_params.yaml'
    )

    nav2_launch_dir = os.path.join(
        get_package_share_directory('nav2_bringup'), 
        'launch'
    )

    navigation_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([nav2_launch_dir, '/bringup_launch.py']),
        launch_arguments={
            'map': map_file,
            'use_sim_time': 'False',
            'params_file': nav_param_file}.items(),
    )

    rviz_file = os.path.join(get_package_share_directory('nav2_pkg'), 'config', 'nav2_rviz2.rviz')
    rviz_cmd = Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            arguments=['-d', rviz_file]
        )

    ld = LaunchDescription()
    ld.add_action(navigation_cmd)
    ld.add_action(rviz_cmd)

    return ld
