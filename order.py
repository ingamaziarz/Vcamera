import numpy as np

def order_painter(faces_list, camera_position):
    faces_list.sort(key=lambda face: np.linalg.norm(camera_position - face.center), reverse=True)