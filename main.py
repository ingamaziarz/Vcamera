from cuboid import *
from operations import *
import pygame
w = 800 #window width
h = 800 #window height
dist = 200
step_dist = 2

window = pygame.display.set_mode((w, h))
pygame.init()
pygame.display.set_caption("Wirtualna kamera")
if __name__=='__main__':
    c1 = Cuboid(vertices=[[50, 50, 100]], dims=(60, 60, 60), color=(200, 0, 150))
    c2 = Cuboid(vertices=[[100, 50, 150]], dims=(60, 50, 60), color=(150, 50, 150))
    c3 = Cuboid(vertices=[[-100, 50, 0]], dims=(100, 60, 100), color=(0, 200, 150))
    c4 = Cuboid(vertices=[[-50, -50, 200]], dims=(100, 60, 60), color=(200, 150, 0))
    c5 = Cuboid(vertices=[[-50, -50, -50]], dims=(100, 200, 100), color=(100, 100, 100))

    cuboids = []
    cuboids.append(c1)
    cuboids.append(c2)
    cuboids.append(c3)
    cuboids.append(c4)
    cuboids.append(c5)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            keys = pygame.key.get_pressed()
            # translation (6 types)
            if keys[pygame.K_d]:
                print("x +")
                trans(cuboids, 0, -1)
            if keys[pygame.K_a]:
                print("x -")
                trans(cuboids, 0, 1)
            if keys[pygame.K_w]:
                print("y +")
                trans(cuboids, 1, 1)
            if keys[pygame.K_s]:
                print("y -")
                trans(cuboids, 1, -1)
            if keys[pygame.K_x]:
                print("z +")
                trans(cuboids, 2, -1)
            if keys[pygame.K_z]:
                print("z -")
                trans(cuboids, 2, +1)

            # rotation (6 types)
            if keys[pygame.K_PERIOD]:
                print("Y axis +")
                rot(cuboids, "y", 1)
            if keys[pygame.K_COMMA]:
                print("Y axis -")
                rot(cuboids, "y", -1)
            if keys[pygame.K_l]:
                print("Z axis +")
                rot(cuboids, "z", -1)
            if keys[pygame.K_k]:
                print("Z axis -")
                rot(cuboids, "z", 1)
            if keys[pygame.K_p]:
                print("X axis +")
                rot(cuboids, "x", 1)
            if keys[pygame.K_o]:
                print("X axis -")
                rot(cuboids, "x", -1)

            #zoom (2 types)
            if keys[pygame.K_MINUS]:
                print("zoom -")
                dist += step_dist
            if keys[pygame.K_EQUALS]:
                print("zoom +")
                dist -= step_dist
            if keys[pygame.K_q]:
                running = False
                pygame.quit()
                raise SystemExit

        window.fill((255, 255, 255))
        for cuboid in cuboids:
            cuboid.draw(window, dist, w, h)
        pygame.display.update()