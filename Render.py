from math import *
from GameConf import *

def ray(pos, angle, mapa, dist=False):
    x, y = pos
    sin_a = sin(angle)
    cos_a = cos(angle)
    d = 2
    distance = 0
    for _ in range(200):
        # [x + distance * cos_a, y + distance * sin_a]
        if any(set([True if a[0] < int(x + distance * cos_a) < a[2] and a[1] < int(y + distance * sin_a) < a[3] else False for a in mapa])):
            break
        else:
            distance += d
    else:
        distance = 2000
    x += distance * cos_a
    y += distance * sin_a
    if dist:
        return distance
    else:
        return [x, y]

