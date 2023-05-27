import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource


from launch_ros.actions import Node
import xacro


def generate_launch_description():

    # Specify the name of the package and path to xacro file within the package
    pkg_name = 'trackingplatform'
    rocketfile_subpath = 'description/rocket.urdf.xacro'


    # Use xacro to process the file
    xacro_file = os.path.join(get_package_share_directory(pkg_name),rocketfile_subpath)
    rocket_description_raw = xacro.process_file(xacro_file).toxml()


    # Configure the node
    node_rocket_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': rocket_description_raw,
        'use_sim_time': True}] # add other parameters here if required
    )

    # gazebo = IncludeLaunchDescription(
    #     PythonLaunchDescriptionSource([os.path.join(
    #         get_package_share_directory('gazebo_ros'), 'launch'), '/gazebo.launch.py']),
    #     )

    spawn_entity = Node(
                        package='gazebo_ros', 
                        executable='spawn_entity.py',
                        arguments=['-topic', 'robot_description',
                                '-entity', 'rocket',
                                '-x', '3',
                                '-z', '1'],
                        output='screen'
                        )

# https://github.com/ros-simulation/gazebo_ros_pkgs/blob/foxy/gazebo_ros/scripts/spawn_entity.py#L51
        # parser.add_argument('-x', type=float, default=0,
        #                     help='x component of initial position, meters')
        # parser.add_argument('-y', type=float, default=0,
        #                     help='y component of initial position, meters')
        # parser.add_argument('-z', type=float, default=0,
        #                     help='z component of initial position, meters')
        # parser.add_argument('-R', type=float, default=0,
        #                     help='roll angle of initial orientation, radians')
        # parser.add_argument('-P', type=float, default=0,
        #                     help='pitch angle of initial orientation, radians')
        # parser.add_argument('-Y', type=float, default=0,
        #                     help='yaw angle of initial orientation, radians')

    # Run the node
    return LaunchDescription([
        # gazebo,
        node_rocket_state_publisher,
        spawn_entity
    ])

