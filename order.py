import numpy as np

def order_painter(faces_list, camera_position):
    faces_list.sort(key=lambda face: np.mean([np.linalg.norm(camera_position - v) for v in face.vertices]), reverse=True)
