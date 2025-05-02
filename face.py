import numpy as np

class Face:
    def __init__(self, all_vertices, idx, color):
        self.vertices = [all_vertices[i] for i in idx] #initial vertices (3d)
        self.projected = []
        self.color = color
        self.center = np.mean(self.vertices, axis=0)
        print("SELF CENTER: ", self.center)



