"""Launch RViz only. For robot_description you must run rsp + move_group (e.g. use demo.launch.py for full stack)."""
from moveit_configs_utils import MoveItConfigsBuilder
from moveit_configs_utils.launches import generate_moveit_rviz_launch


def generate_launch_description():
    moveit_config = MoveItConfigsBuilder("so101_new_calib", package_name="lerobot_moveit").to_moveit_configs()
    return generate_moveit_rviz_launch(moveit_config)
