import numpy as np

class Face:
    def __init__(self, vertices, all_vertices, normal, idx, color):
        if vertices is not None and normal is not None:
            self.vertices = vertices
            self.normal = normal
        elif all_vertices is not None and idx is not None:
            self.vertices = [all_vertices[i] for i in idx]  # initial vertices (3d)
            v1 = np.array(self.vertices[1]) - np.array(self.vertices[0])
            v2 = np.array(self.vertices[2]) - np.array(self.vertices[0])
            normal = np.cross(v1, v2)
            norm = np.linalg.norm(normal)
            self.normal = normal / norm if norm != 0 else normal

        self.projected = []
        self.color = color
        self.center = np.mean(self.vertices, axis=0)
