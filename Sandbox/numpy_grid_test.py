import numpy as np
import math

def test():
    valid_coords = []
    for i in range(100):
        for j in range(100):
            valid_coords.append((j, i))
    for i in range(25):
        for j in range(25):
            valid_coords.remove((j, i))
    (1, 1) in valid_coords


def test2():
    val_coords = np.random.rand(100, 100)
    val_coords[:25, :25] = 0
    val_coords[np.where(val_coords != 0)] = 1


def test3():
    math.sqrt(math.pi * math.pi * math.pi - 1.123123123123123)

import time
ts = time.time()
for i in range(1000):
    test2()
print(time.time() - ts)
