import matplotlib.pyplot as plt
import numpy as np
from vectortools3D import Vector
from objects import *
height = 100
width = 200

img = np.zeros((100, 200, 3))

for i in range(100):
    for j in range(200):
        r = i/height
        g = j/width
        b = 0.2
        img[i][j] = Vector(r,g,b).list()
        
plt.imshow(img)
plt.show()

class Ray:
    def __init__(self, p, u):
        self.p = p
        self.u = u/abs(u)
        
class Light:
    def __init__(self, p):
        self.p = p
     
s=10
height = 100*s
width = 200*s

half_h = height//2
half_w = width//2

o = Vector(100, 50, 40)*s
r = 20*s
s1 = Sphere(o, r)

o = Vector(50, 50, 70)*s
r = 20*s
s2 = Sphere(o, r)

o = Vector(150, 80, 40)*s
v = Vector(0, -1, -0.5)
r = 20*s
h = 60*s
cy1 = Cynlinder(o, v, r, h)

o = o + h*cy1.v
n = v
r = 20*s
c1 = Circle(o, n, r)

o = Vector(100, 80, 40)*s
n = Vector(0, -1, -0.5)
r = 100*s
c2 = Circle(o, n, r)

objects = [s1, s2, c1, cy1, c2]
for k in [40]:#range(100):
    p = Vector(50+k, 0, 0)*s
    l1 = Light(p)
    img = np.full((height, width, 3),(0.3,0.8,0.9))

    for i in range(height):
        for j in range(width):
            p = Vector(j, i, -10*s)
            u = Vector(0.01*(j-half_w)/width, 0.01*(i-half_h)/height, 1)
            ray = Ray(p, u)
            for ob in objects:
                t = ob.hit(ray)
                if t:
                    hit_p = ray.p+ray.u*t
                    l = hit_p-l1.p
                    l = l/abs(l)
                    v = ray.p - hit_p
                    v = v/abs(v)
                    r = l - 2*ob.n.dot(l)*ob.n
                    r = r/abs(r)
                    phong = ( - 1*Vector(0.5,0.5,0.5)*min(0,ob.n.dot(l)) + Vector(0.3,0.3,0.3)*max(0, v.dot(r))**14)
                    bias = 0.2*s
                    shadow_ray = Ray(hit_p+ob.n*bias, -1*l)

                    K=1
                    for ob in objects:
                        shadow_t = ob.hit(shadow_ray)
                        if shadow_t:
                            K=0

                    img[i][j] = (Vector(0.2, 0.2, 0.2)+K*phong).list()
                    break
    #plt.figure(dpi=600)
    plt.imshow(img)
    plt.show()
    #plt.imsave('/content/drive/My Drive/Colab Notebooks/ray tracing/raytracing'+str(k)+'.png', img)
