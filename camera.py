import numpy as np

step_len = 2
step_rad = 0.005

class Camera:
    def __init__(self):
        self.position = np.array([-100.0, 100.0, -300.0])
        self.rotation = np.eye(3)

    def trans(self, dim, dir):
        trans_matrix = np.zeros(3)
        trans_matrix[dim] = dir * step_len
        self.position += self.rotation @ trans_matrix

    def rot(self, dim, dir):
        a = step_rad * dir
        if dim == "x":
            rot_matrix = np.array([
                [1, 0, 0],
                [0, np.cos(a), -np.sin(a)],
                [0, np.sin(a),  np.cos(a)]
            ])
        elif dim == "y":
            rot_matrix = np.array([
                [np.cos(a), 0, np.sin(a)],
                [0, 1, 0],
                [-np.sin(a), 0, np.cos(a)]
            ])
        elif dim == "z":
            rot_matrix = np.array([
                [np.cos(a), -np.sin(a), 0],
                [np.sin(a),  np.cos(a), 0],
                [0, 0, 1]
            ])
        self.rotation = self.rotation @ rot_matrix

    def get_projection_matrix(self):
        projection_matrix = np.eye(4)
        projection_matrix[:3, :3] = self.rotation
        projection_matrix[:3, 3] = - self.rotation @ self.position
        return projection_matrix
