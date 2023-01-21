import math

numbers = input("in: ")

n = float(numbers.split(",")[0])
a = float(numbers.split(",")[1])

result = n/4 * 1/(math.tan(math.pi/n)) * a**2

print("out: " + str(result))