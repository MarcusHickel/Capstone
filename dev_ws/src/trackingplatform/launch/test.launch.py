import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch.actions import RegisterEventHandler
from launch.event_handlers import OnProcessExit

from launch_ros.actions import Node
import xacro

from launch.actions import DeclareLaunchArgument, ExecuteProcess
from launch.substitutions import LaunchConfiguration, Command, PathJoinSubstitution

def generate_launch_description():

    # Specify the name of the package and path to xacro file within the package
    pkg_name = 'trackingplatform'
    file_subpath = 'description/robot.urdf.xacro'


    # Use xacro to process the file
    xacro_file = os.path.join(get_package_share_directory(pkg_name),file_subpath)
    robot_description_raw = xacro.process_file(xacro_file).toxml()


    # Run the node
    return LaunchDescription([

        DeclareLaunchArgument(
            name='world', 
            default_value='/home/marcus/rockettrackingplatform/dev_ws/src/trackingplatform/world/world',
            description='Gazebo world'
        ),

        ExecuteProcess(
            cmd=['gazebo', '--verbose', '-s', 'libgazebo_ros_factory.so',  '-s', 'libgazebo_ros_init.so', LaunchConfiguration('world')],
            output='screen'
        ),

        Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot_description_raw,
        'use_sim_time': True}] # add other parameters here if required
        ),

        Node(
            package='gazebo_ros', 
            # namespace='cameraplatform',
            executable='spawn_entity.py',
            arguments=['-topic', 'robot_description',
                        '-entity', 'my_bot'],
            output='screen'
            ),

        Node(
        package="controller_manager",
        executable="spawner.py",
        arguments=["joint_broad"],
        ),

        Node(
        package="controller_manager",
        executable="spawner.py",
        arguments=["forward_position_controller", "--controller-manager", "/controller_manager"],
        )
    
    ])

