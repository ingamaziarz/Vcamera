from cuboid import *
from camera import *
import pygame
import os
w = 800 #window width
h = 800 #window height
dist = 500
step_dist = 0.5

window = pygame.display.set_mode((w, h))
pygame.init()
pygame.display.set_caption("Wirtualna kamera")
if __name__=='__main__':
    camera = Camera()
    cuboids = [Cuboid(vertices=[[50, 50, 50]], dims=(50, 50, 50), color=(200, 0, 0)),
               Cuboid(vertices=[[150, 50, 50]], dims=(50, 50, 50), color=(0, 0, 200)),
               Cuboid(vertices=[[50, 50, -50]], dims=(50, 50, 50), color=(0, 200, 0))]

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
            print("x +")
            camera.trans(0, 1)
        if keys[pygame.K_a]:
            print("x -")
            camera.trans(0, -1)
        if keys[pygame.K_w]:
            print("y +")
            camera.trans(1, 1)
        if keys[pygame.K_s]:
            print("y -")
            camera.trans(1, -1)
        if keys[pygame.K_x]:
            print("z +")
            camera.trans(2, 1)
        if keys[pygame.K_z]:
            print("z -")
            camera.trans(2, -1)

        # rotation (6 types)
        if keys[pygame.K_PERIOD]:
            print("Y axis +")
            camera.rot("y", 1)
        if keys[pygame.K_COMMA]:
            print("Y axis -")
            camera.rot("y", -1)
        if keys[pygame.K_l]:
            print("Z axis +")
            camera.rot("z", -1)
        if keys[pygame.K_k]:
            print("Z axis -")
            camera.rot("z", 1)
        if keys[pygame.K_p]:
            print("X axis +")
            camera.rot("x", -1)
        if keys[pygame.K_o]:
            print("X axis -")
            camera.rot("x", 1)

        # zoom (2 types)
        if keys[pygame.K_MINUS]:
            print("zoom -")
            dist -= step_dist

        if keys[pygame.K_EQUALS]:
            print("zoom +")
            dist += step_dist

        window.fill((255, 255, 255))

        view_matrix = camera.get_view_matrix()

        for cuboid in cuboids:
            projected_vertices = []
            for vertex in cuboid.vertices:
                cam_view_coords = view_matrix @ vertex
                z = cam_view_coords[2]
                f = dist / z
                x = cam_view_coords[0] * f + w / 2
                y = -cam_view_coords[1] * f + h / 2
                projected_vertices.append((x, y))

            for edge in cuboid.edges:
                pygame.draw.line(window, cuboid.color, projected_vertices[edge[0]], projected_vertices[edge[1]], 5)
        pygame.display.update()