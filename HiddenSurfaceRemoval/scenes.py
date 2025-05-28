from cuboid import *

def create_scene(option):
    cuboids = []
    match option:
        case "blocks":
            c1 = Cuboid(vertices=[[50, 50, 100]], dims=(60, 60, 60), color=(200, 0, 150))
            c2 = Cuboid(vertices=[[100, 50, 150]], dims=(60, 50, 60), color=(150, 50, 150))
            c3 = Cuboid(vertices=[[-100, 50, 0]], dims=(100, 60, 100), color=(0, 200, 150))
            c4 = Cuboid(vertices=[[-50, -50, 200]], dims=(100, 60, 60), color=(200, 150, 0))
            c5 = Cuboid(vertices=[[-50, -50, -50]], dims=(100, 200, 100), color=(100, 100, 100))
            cuboids.append(c1)
            cuboids.append(c2)
            cuboids.append(c3)
            cuboids.append(c4)
            cuboids.append(c5)
            return cuboids

        case "street":
            block1 = Cuboid(vertices=[[-100, 0, 50]], dims=(50, -200, 50), color=(100, 100, 100))
            block2 = Cuboid(vertices=[[-100, 0, 150]], dims=(60, -150, 50), color=(150, 150, 150))
            block3 = Cuboid(vertices=[[-100, 0, 250]], dims=(50, -300, 60), color=(200, 200, 200))
            block4 = Cuboid(vertices=[[100, 0, 100]], dims=(70, -150, 100), color=(0, 0, 0))
            grass = Cuboid(vertices=[[-120, -20, 0]], dims=(300, -15, 350), color=(20, 200, 20))

            cuboids.append(block1)
            cuboids.append(block2)
            cuboids.append(block3)
            cuboids.append(block4)
            cuboids.append(grass)
            return cuboids

        case "cube":
            block_size = (30, -30, 30)
            gap = 5

            start_x, start_y, start_z = -50, 0, -50

            for i in range(3):
                for j in range(3):
                    for k in range(3):
                        x = start_x + i * (block_size[0] + gap)
                        y = start_y + j * (block_size[1] - gap)
                        z = start_z + k * (block_size[2] + gap)

                        color = (255 if i == 0 else (128 if i == 1 else 0),
                                 255 if j == 1 else (128 if j == 2 else 0),
                                 255 if k == 2 else (128 if k == 0 else 0))
                        cuboids.append(Cuboid(vertices=[[x, y, z]], dims=block_size, color=color))
            return cuboids

        case default:
            cuboids = [Cuboid(vertices=[[0, 0, 0]], dims=(50, 50, 50), color=(200, 0, 0)),
                       Cuboid(vertices=[[100, 0, 0]], dims=(50, 50, 50), color=(0, 0, 200)),
                       Cuboid(vertices=[[0, 0, -100]], dims=(50, 50, 50), color=(0, 200, 0))]
            return cuboids