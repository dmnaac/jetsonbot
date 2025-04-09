from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    base_node = Node(
        package = "tf2_ros",
        executable = "static_transform_publisher",
        output = "screen",
        arguments = ["0", "0", "0", "0", "0", "0", "base_footprint", "base_link"]
        )
    
    laser_node = Node(
        package="tf2_ros",
        executable="static_transform_publisher",
        output="screen",
        arguments=["0.188", "0.0", "0.39", "0", "0", "0", "base_link", "laser"]
        )
    
    realsense_node = Node(
        package="tf2_ros",
        executable="static_transform_publisher",
        output="screen",
        arguments=["0", "0", "0", "0", "0", "0", "base_link", "camera"]
        )
    
    imu_node = Node(
        package="tf2_ros",
        executable="static_transform_publisher",
        output="screen",
        arguments=["0.14", "0.0", "0.0", "0", "0", "3.14", "base_link", "imu"]
        )
    
    ld = LaunchDescription()
    ld.add_action(base_node)
    ld.add_action(laser_node)
    ld.add_action(realsense_node)
    ld.add_action(imu_node)

    return ld