import numpy as np
step_len = 5
step_rad = 0.005

class Camera:
    def __init__(self):
        self.camera_state = np.eye(4)
        self.camera_state[:3, 3] = [0.0, 0.0, -400.0]
        self.position = [0.0, 0.0, -400.0]

    def trans(self, dim, dir):
        trans_matrix = np.eye(4)
        trans_matrix[dim, 3] = dir * step_len
        self.camera_state = self.camera_state @ trans_matrix

    def rot(self, dim, dir):
        a = step_rad * dir
        if dim == "x":
            rot_matrix = np.array([
                [1, 0, 0, 0],
                [0, np.cos(a), -np.sin(a), 0],
                [0, np.sin(a),  np.cos(a), 0],
                [0, 0, 0, 1]
            ])
        elif dim == "y":
            rot_matrix = np.array([
                [np.cos(a), 0, np.sin(a), 0],
                [0, 1, 0, 0],
                [-np.sin(a), 0, np.cos(a), 0],
                [0, 0, 0, 1]
            ])
        elif dim == "z":
            rot_matrix = np.array([
                [np.cos(a), -np.sin(a), 0, 0],
                [np.sin(a),  np.cos(a), 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1]
            ])

        self.camera_state = self.camera_state @ rot_matrix

    def get_view_matrix(self):
        return np.linalg.inv(self.camera_state)

    def update_camera_position(self):
        self.position = self.camera_state[:3, 3]