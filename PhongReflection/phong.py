import numpy as np
import matplotlib.pyplot as plt

w = 200
h = 200

image = np.zeros((h, w, 3))

r = 0.7  # sphere radius
sphere_color = np.array([0, 1, 0])
#sphere is located at (0,0,0)

light_pos = np.array([1, 0, 2.5])
light_color = np.array([1.0, 1.0, 1.0])

view_pos = np.array([0.0, 0.0, 0.0])

k_a = 0.5
k_d = 0.5
k_s = 0.5
n = 25

I_a = 0.3
I_p = 1.0

# attenuation: constant, linear & quadratic components
att_0 = 1.0
att_1 = 0.2
att_2 = 0.02

x_coords = np.linspace(-1, 1, w)
y_coords = np.linspace(-1, 1, h)
X, Y = np.meshgrid(x_coords, y_coords)

for i in range(h):
    for j in range(w):
        x = X[i, j]
        y = Y[i, j]

        if x**2 + y**2 <= r**2:
            z = np.sqrt(r**2 - x**2 - y**2)
            P = np.array([x, y, z])
            N = P / np.linalg.norm(P)

            L = light_pos - P
            L_dist = np.linalg.norm(L)
            L = L / L_dist

            H = L + view_pos
            H = H / np.linalg.norm(H)

            attenuation = 1.0 / (att_0 + att_1 * L_dist + att_2 * (L_dist**2))
            ambient = I_a * k_a * sphere_color
            diffuse = I_p * k_d * (N @ L) * light_color * sphere_color
            specular = I_p * k_s * (N @ H)**n * light_color

            image[i, j] = np.clip(ambient + attenuation * (diffuse + specular), 0, 1)
        else:
            image[i, j] = [0.0, 0.0, 0.4] # background

plt.imshow(image)
plt.axis("off")
plt.show()