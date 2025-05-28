import pygame
import os # to force close window
from scenes import *
from bsp import *
w = 800 #window width
h = 800 #window height
dist = 500
step_dist = 3

window = pygame.display.set_mode((w, h))
pygame.init()
pygame.display.set_caption("Wirtualna kamera")

if __name__ == '__main__':
    camera = Camera()
    #options: "blocks", "street", "cube"
    cuboids = create_scene(option="street")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                os._exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    os._exit(0)

        keys = pygame.key.get_pressed()
        # camera.translation (6 types)
        if keys[pygame.K_d]:
            #print("x +")
            camera.trans(0, 1)
        if keys[pygame.K_a]:
            #print("x -")
            camera.trans(0, -1)
        if keys[pygame.K_w]:
            #print("y +")
            camera.trans(1, 1)
        if keys[pygame.K_s]:
            #print("y -")
            camera.trans(1, -1)
        if keys[pygame.K_x]:
            #print("z +")
            camera.trans(2, 1)
        if keys[pygame.K_z]:
            #print("z -")
            camera.trans(2, -1)

        # rotation (6 types)
        if keys[pygame.K_PERIOD]:
            #print("Y axis +")
            camera.rot("y", 1)
        if keys[pygame.K_COMMA]:
            #print("Y axis -")
            camera.rot("y", -1)
        if keys[pygame.K_l]:
            #print("Z axis +")
            camera.rot("z", -1)
        if keys[pygame.K_k]:
            #print("Z axis -")
            camera.rot("z", 1)
        if keys[pygame.K_p]:
            #print("X axis +")
            camera.rot("x", -1)
        if keys[pygame.K_o]:
            #print("X axis -")
            camera.rot("x", 1)

        #zoom (2 types)
        if keys[pygame.K_MINUS]:
            #print("zoom -")
            dist -= step_dist
        if keys[pygame.K_EQUALS]:
            #print("zoom +")
            dist += step_dist

        window.fill((255, 255, 255))

        all_faces = []
        for cuboid in cuboids:
            all_faces.extend(cuboid.faces)

        camera.update_camera_position()
        ordered_faces = order_bsp(all_faces, camera)

        projection_matrix = camera.get_view_matrix()

        for face in ordered_faces:
            cam_to_face = face.center - camera.position
            if np.dot(face.normal, cam_to_face) < 0: # do not draw back faces
                continue

            projected_vertices = []
            for vertex in face.vertices:
                vertex_extended = np.append(vertex, 1)
                cam_coords = projection_matrix @ vertex_extended

                z = cam_coords[2]

                f = dist / z
                x = cam_coords[0] * f + w / 2
                y = -cam_coords[1] * f + h / 2
                projected_vertices.append((x, y))
            pygame.draw.polygon(window, face.color, projected_vertices)


        pygame.display.update()

    pygame.quit()

