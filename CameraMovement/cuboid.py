class Cuboid:
    def __init__(self, vertices, dims, color=(0, 0, 0)):
        if len(vertices) == 8 and dims is None:
            self.vertices = vertices
        elif len(dims) == 3 and len(vertices) == 1: #then compute all vertices
            #starting vertex
            x, y, z = vertices[0]
            a = dims[0] #length
            b = dims[1] #height
            c = dims[2] #depth
            #finish top base
            vertices.append([x, y, z + c])
            vertices.append([x + a, y, z + c])
            vertices.append([x + a, y, z])
            #bottom base
            vertices.append([x, y + b, z])
            vertices.append([x, y + b, z + c])
            vertices.append([x + a, y + b, z + c])
            vertices.append([x + a, y + b, z])

            [vertex.append(1) for vertex in vertices]
            self.vertices = vertices
            print(self.vertices)
        self.edges = [(0, 1), (1, 2), (2, 3), (3, 0),
                      (4, 5), (5, 6), (6, 7), (7, 4),
                      (0, 4), (1, 5), (2, 6), (3, 7)]
        self.color = color
