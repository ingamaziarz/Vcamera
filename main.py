import pygame
from order import *
from scenes import *
from camera import *

w = 800 #window width
h = 800 #window height
dist = 200
step_dist = 2

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
                running = False
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
            camera.rot("y", -1)
        if keys[pygame.K_COMMA]:
            print("Y axis -")
            camera.rot("y", 1)
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

        projection_matrix = camera.get_projection_matrix()

        for cuboid in cuboids:
            cuboid.project(projection_matrix, dist, w, h)
            faces.extend(cuboid.faces)

        order_painter(faces, camera.position)
        for face in faces:
            pygame.draw.polygon(window, face.color, face.projected)

        pygame.display.update()
