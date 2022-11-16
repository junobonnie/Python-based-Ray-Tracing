import math as m
from vectortools3D import Vector

class Circle:
    def __init__(self, o, n, r):
        self.o = o
        self.n = n/abs(n)
        self.r = r
        self._bias = 0.001

    def hit(self, ray):
        d = ray.p-self.o
        t = -d.dot(self.n)/(ray.u.dot(self.n)+self._bias)
        if t > 0:
            r_ = d + ray.u*t
            if r_.dot(r_) < self.r**2:
                return t
        return False
        
class Sphere:
    def __init__(self, o, r):
        self.o = o
        self.r = r

    def hit(self, ray):
        d = ray.p - self.o
        F = (ray.u.dot(d))**2-(d.dot(d)-self.r**2)
        if F > 0:
            t1 = -ray.u.dot(d)-m.sqrt(F)
            t2 = -ray.u.dot(d)+m.sqrt(F)
            t = min(t1, t2)
            if t > 0:
                n = (d+ray.u*t)
                self.n = n/abs(n)
                return t
        return False

class Cynlinder:
    def __init__(self, o, v, r, h):
        self.o = o
        self.v = v/abs(v)
        self.r = r
        self.h = h
        self._bias = 0.001

    def hit(self, ray):
        d = ray.p - self.o
        
        a = 1-(ray.u.dot(self.v))**2
        b = ray.u.dot(d) - self.v.dot(ray.u)*self.v.dot(d)
        c = d.dot(d) - d.dot(self.v)**2 - self.r**2

        F = b**2-a*c

        if F > 0:
            t1 = (-b-m.sqrt(F))/(a + self._bias)
            t2 = (-b+m.sqrt(F))/(a + self._bias)
            t = min(t1, t2)
            if t > 0:
                r = d+ray.u*t
                H = r.dot(self.v)
                if 0 < H < self.h:
                    n = r - H*self.v
                    self.n = n/abs(n)
                    return t
        return False

class Cone:
    def __init__(self):
        pass
