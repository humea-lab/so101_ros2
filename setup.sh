#!/usr/bin/env bash
# One-command setup: install dependencies and build the workspace.
# Run from workspace root after cloning. Requires ROS 2 to be sourced (e.g. source /opt/ros/<distro>/setup.bash).
set -e
echo "[setup] Updating rosdep..."
rosdep update
echo "[setup] Installing dependencies from src..."
rosdep install --from-paths src --ignore-src -r -y
echo "[setup] Building workspace..."
colcon build --symlink-install
echo "[setup] Done. Source the workspace with: source install/setup.bash"
