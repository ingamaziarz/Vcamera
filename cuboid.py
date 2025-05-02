import pygame
import numpy as np
from face import *

class Cuboid:
    def __init__(self, vertices, dims, color=(0, 0, 0)):
        if len(vertices) == 8 and dims is None:
            self.vertices = vertices
        elif len(dims) == 3 and len(vertices) == 1: #then compute all vertices
            #starting vertex: left, highest, deepest
            x, y, z = vertices[0] #id=0
            a = dims[0] #length
            b = dims[1] #height
            c = dims[2] #depth
            #finish top base
            vertices.append([x + a, y, z]) #id=1
            vertices.append([x + a, y, z + c]) #id=2
            vertices.append([x, y, z + c]) #id=3

            #bottom base:
            vertices.append([x, y - b, z]) #id=4
            vertices.append([x, y - b, z + c]) #id=5
            vertices.append([x + a, y - b, z + c]) #id=6
            vertices.append([x + a, y - b, z]) #id=7
            [vertex.append(1) for vertex in vertices]
            self.vertices = vertices

        #initialize 6 faces, each using 4 vertices numbered clockwise (CW) considering they are FRONT
        self.faces_vertices_idx = [(0, 1, 2, 3), (4, 5, 6, 7), (3, 2, 6, 5), (2, 1, 7, 6), (1, 0, 4, 7), (0, 3, 5, 4)]
        self.faces = [Face(vertices, idx, color) for idx in self.faces_vertices_idx]
        self.color = color

    def project(self, dist, w, h):
        projected = []
        projection_matrix = np.eye(4)
        projection_matrix[2][2] /= dist

        for vertex in self.vertices:
            z = vertex[2]
            result = (projection_matrix @ vertex) * dist / (z + dist)
            projected.append([result[0] + w / 2, result[1] + h / 2])

        for i, face in enumerate(self.faces):
            idx = self.faces_vertices_idx[i]
            face.projected = [projected[id] for id in idx]

        self.projected = projected
