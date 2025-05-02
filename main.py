from cuboid import *
from operations import *
from order import *
from scenes import *
import pygame
w = 800 #window width
h = 800 #window height
dist = 200
step_dist = 2

window = pygame.display.set_mode((w, h))
pygame.init()
pygame.display.set_caption("Wirtualna kamera")
if __name__=='__main__':
    camera_position = [0, 0, 0, 1]

    cuboids = create_scene(option="street")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            keys = pygame.key.get_pressed()
            # translation (6 types)
            if keys[pygame.K_d]:
                print("x +")
                trans(cuboids, 0, -1, camera_position)
            if keys[pygame.K_a]:
                print("x -")
                trans(cuboids, 0, 1, camera_position)
            if keys[pygame.K_w]:
                print("y +")
                trans(cuboids, 1, 1, camera_position)
            if keys[pygame.K_s]:
                print("y -")
                trans(cuboids, 1, -1, camera_position)
            if keys[pygame.K_x]:
                print("z +")
                trans(cuboids, 2, -1, camera_position)
            if keys[pygame.K_z]:
                print("z -")
                trans(cuboids, 2, 1, camera_position)

            # rotation (6 types)
            if keys[pygame.K_PERIOD]:
                print("Y axis +")
                rot(cuboids, "y", 1, camera_position)
            if keys[pygame.K_COMMA]:
                print("Y axis -")
                rot(cuboids, "y", -1, camera_position)
            if keys[pygame.K_l]:
                print("Z axis +")
                rot(cuboids, "z", -1, camera_position)
            if keys[pygame.K_k]:
                print("Z axis -")
                rot(cuboids, "z", 1, camera_position)
            if keys[pygame.K_p]:
                print("X axis +")
                rot(cuboids, "x", 1, camera_position)
            if keys[pygame.K_o]:
                print("X axis -")
                rot(cuboids, "x", -1, camera_position)

            #zoom (2 types)
            if keys[pygame.K_MINUS]:
                print("zoom -")
                dist -= step_dist
            if keys[pygame.K_EQUALS]:
                print("zoom +")
                dist += step_dist
            if keys[pygame.K_q]:
                running = False
                pygame.quit()
                raise SystemExit

        window.fill((255, 255, 255))
        faces = []

        for cuboid in cuboids:
            cuboid.project(dist, w, h)
            faces.extend(cuboid.faces)

        order_painter(faces, camera_position)
        for face in faces:
            pygame.draw.polygon(window, face.color, face.projected)

        pygame.display.update()