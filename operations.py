import numpy as np
step_len = 10
step_rad = 0.02 #step in radians

def trans(cuboids, dim, dir):
    trans_matrix = np.eye(4)
    trans_matrix[dim][3] = dir * step_len
    for cuboid in cuboids:
        cuboid.vertices = [trans_matrix @ vertex for vertex in cuboid.vertices]

def rot(cuboids, dim, dir):
    rot_matrix = np.eye(4)
    a = step_rad * dir
    if dim == "x":
        rot_matrix[1:3] = [0, np.cos(a), -np.sin(a), 0], [0, np.sin(a), np.cos(a), 0]
    elif dim == "y":
        rot_matrix[0] = [np.cos(a), 0, np.sin(a), 0]
        rot_matrix[2] = [-np.sin(a), 0, np.cos(a), 1]
    elif dim == "z":
        rot_matrix[0:2] = [np.cos(a), -np.sin(a), 0, 0], [np.sin(a), np.cos(a), 0, 0]

    for cuboid in cuboids:
        cuboid.vertices = [rot_matrix @ vertex for vertex in cuboid.vertices]
