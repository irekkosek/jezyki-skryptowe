import random
import math

ins = 0
total = 100000

for i in range(0, total):

    x2 = random.random()**2
    y2 = random.random()**2

    if math.sqrt(x2 + y2) < 1.0:
        ins += 1

pi = (float(ins) / total) * 4

print(pi)