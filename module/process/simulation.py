""" Outer library """
import numpy
from PIL import Image

""" Processes """
# Simulation
def simulation(learntime, x = 64, y = 64):
    weight = numpy.random.random([x, y, 3])

    imgs = []
    for time in range(learntime):
        color = numpy.random.rand(3)
        weight = som(weight, color, x, y)
        if time % max(int(learntime / 200), 0) == 0:
            imgs.append(Image.fromarray((weight * 255).astype(numpy.uint8)))

    return imgs

# SOM
def som(w, colorvec, x = 64, y = 64):
    alpha = 0.05
    min_index = numpy.argmin(((w - colorvec) ** 2).sum(axis = 2))
    mini = int(min_index / y)
    minj = int(min_index % y)
    for i in range(-2, 3):
        for j in range(-2, 3):
            try:
                w[mini + i, minj + j] += alpha * (colorvec - w[mini + i, minj + j]) / (abs(i) + abs(j) + 1)
            except:
                pass
            
    return w