from face import *

class Cuboid:
    def __init__(self, vertices, dims, color):
        if len(vertices) == 8 and dims is None:
            self.vertices = vertices
        elif len(dims) == 3 and len(vertices) == 1:  #then compute all vertices
            #starting vertex: left, highest, deepest
            x, y, z = vertices[0]  #id=0
            a = dims[0]  # length
            b = dims[1]  # height
            c = dims[2]  # depth
            #finish top base
            vertices.append([x + a, y, z])  #id=1
            vertices.append([x + a, y, z + c])  #id=2
            vertices.append([x, y, z + c])  #id=3

            #bottom base:
            vertices.append([x, y - b, z])  #id=4
            vertices.append([x, y - b, z + c])  #id=5
            vertices.append([x + a, y - b, z + c])  #id=6
            vertices.append([x + a, y - b, z])  #id=7
            self.vertices = vertices

        #initialize 6 faces, each using 4 vertices numbered clockwise (CW) considering they are FRONT
        self.faces_vertices_idx = [(0, 1, 2, 3), (4, 5, 6, 7), (3, 2, 6, 5), (2, 1, 7, 6), (1, 0, 4, 7), (0, 3, 5, 4)]
        self.faces = [Face(vertices, idx, color) for idx in self.faces_vertices_idx]
        self.color = color

    def project(self, projection_matrix, dist, w, h):
        for face in self.faces:
            projected = []
            for vertex in face.vertices:
                vertex_extended = np.append(vertex, 1)
                cam_coords = projection_matrix @ vertex_extended
                z = cam_coords[2]
                f = 0 if not z else dist / z

                x = cam_coords[0] * f + w / 2
                y = -cam_coords[1] * f + h / 2

                projected.append((x, y))
            face.projected = projected
