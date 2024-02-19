"""
Author: Leopold Klotz
Location for running: learm_ws/src/get_dims.py
Purpose: Calculate the bounding box dimensions of STL files
This file was used to get dimensions for the inertial properties of the URDF
"""


from stl import mesh
import numpy as np

def calculate_bounding_box(stl_filename):
    # Load the STL file
    your_mesh = mesh.Mesh.from_file(stl_filename)

    # Get the bounding box dimensions
    min_coords, max_coords = np.min(your_mesh.v0, axis=0), np.max(your_mesh.v0, axis=0)
    bounding_box_dimensions = max_coords - min_coords

    return bounding_box_dimensions

if __name__ == "__main__":
    prepath = "learm_ros2_description/meshes/"
    filenames = [
        "base.stl",
        "shoulder.stl",
        "humerus.stl",
        "forearm.stl",
        "wrist.stl",
        "hand.stl",
        "carpal-left.stl",
        "carpal-right.stl",
        "tendon.stl",
        "finger.stl"
    ]
    stl_filenames = [prepath + filename for filename in filenames]

    for stl_filename in stl_filenames:
        bounding_box_dimensions = calculate_bounding_box(stl_filename)
        print(f"File: {stl_filename}, Bounding box dimensions (x, y, z):", bounding_box_dimensions)
