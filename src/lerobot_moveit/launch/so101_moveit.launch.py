"""MoveIt only: move_group + RViz (no Gazebo). Requires robot state from elsewhere or use for planning demo."""
from moveit_configs_utils import MoveItConfigsBuilder
from moveit_configs_utils.launches import generate_demo_launch


def generate_launch_description():
    moveit_config = (
        MoveItConfigsBuilder("so101_new_calib", package_name="lerobot_moveit")
        .to_moveit_configs()
    )
    return generate_demo_launch(moveit_config)
