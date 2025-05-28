import numpy as np
from face import Face
from camera import Camera

EPSILON = 1e-6

COPLANAR = 0
FRONT = 1
BACK = 2
SPANNING = 3


class BSPNode:
    def __init__(self, face: Face):
        self.face = face
        self.front = None
        self.back = None

def classify_point(point, plane_face):
    dot_product = np.dot(plane_face.normal, point - plane_face.center)

    if dot_product > EPSILON:
        return FRONT
    elif dot_product < -EPSILON:
        return BACK
    else:
        return COPLANAR


def classify_face(face, plane_face):
    front_count, back_count, coplanar_count = 0, 0, 0

    for vertex in face.vertices:
        classification = classify_point(vertex, plane_face)

        if classification == FRONT:
            front_count += 1
        elif classification == BACK:
            back_count += 1
        else:
            coplanar_count += 1

    if not back_count: #coplanar is treated as front
        return FRONT
    elif not front_count:
        return BACK
    else: #some front, some back
        return SPANNING


def get_intersection_point(p1, p2, plane_face):
    d1 = np.dot(plane_face.normal, p1 - plane_face.center)
    d2 = np.dot(plane_face.normal, p2 - plane_face.center)

    t = -d1 / (d2 - d1)
    intersection_point = p1 + t * (p2 - p1)
    return intersection_point


def split_face(face_to_split, plane_face):
    front_vertices = []
    back_vertices = []
    vertices = [np.array(v) for v in face_to_split.vertices]

    for i in range(len(vertices)):
        p1 = vertices[i]
        p2 = vertices[(i + 1) % len(vertices)]

        c1 = classify_point(p1, plane_face)
        c2 = classify_point(p2, plane_face)

        if c1 != BACK:
            front_vertices.append(p1.tolist())
        if c1 != FRONT:
            back_vertices.append(p1.tolist())

        if c1 + c2 == 3: #one back, one front
            intersection = get_intersection_point(p1, p2, plane_face).tolist()
            front_vertices.append(intersection)
            back_vertices.append(intersection)

    front_face_split = Face(vertices=[np.array(v) for v in front_vertices], all_vertices=None, normal=face_to_split.normal, idx=None, color=face_to_split.color)
    back_face_split = Face(vertices=[np.array(v) for v in back_vertices], all_vertices=None, normal=face_to_split.normal, idx=None, color=face_to_split.color)

    return front_face_split, back_face_split


def build_bsp_tree(faces):
    if not faces:
        return None
    root_face = faces[0]
    node = BSPNode(root_face)

    front_list = []
    back_list = []

    for face in faces[1:]:
        classification = classify_face(face, root_face)

        if classification == FRONT or classification == COPLANAR:
            print("FRONT face detected")
            front_list.append(face)
        elif classification == BACK:
            print("BACK face detected")
            back_list.append(face)

        elif classification == SPANNING:
            print("SPANNING face detected. Splitting...")
            split_result = split_face(face, root_face)
            if split_result:
                front_part, back_part = split_result
                if front_part:
                    print("SPANNING front part found.")
                    front_list.append(front_part)
                if back_part:
                    print("SPANNING back part found.")
                    back_list.append(back_part)

    #building subtrees recursively
    node.front = build_bsp_tree(front_list)
    node.back = build_bsp_tree(back_list)

    return node


#traverse inorder
def traverse_bsp(node, camera_position):
    if node is None:
        return []

    ordered_faces = []
    camera_side = classify_point(camera_position, node.face)

    if camera_side == BACK:
        ordered_faces.extend(traverse_bsp(node.front, camera_position))
        ordered_faces.append(node.face)
        ordered_faces.extend(traverse_bsp(node.back, camera_position))

    else:
        ordered_faces.extend(traverse_bsp(node.back, camera_position))
        ordered_faces.append(node.face)
        ordered_faces.extend(traverse_bsp(node.front, camera_position))

    return ordered_faces

bsp_tree = None

def order_bsp(faces_list, camera):
    global bsp_tree
    if bsp_tree is None:
        print("Building BSP Tree...")
        bsp_tree = build_bsp_tree(faces_list)
        if bsp_tree:
             print("BSP Tree Built.")

    ordered_list = traverse_bsp(bsp_tree, camera.position)
    return ordered_list