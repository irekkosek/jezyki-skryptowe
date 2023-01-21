import random

def randomItem(input):
    return input[random.randint(0, len(input)-1)]

input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(randomItem(input))

