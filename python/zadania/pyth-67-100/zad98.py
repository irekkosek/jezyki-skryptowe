import cmath

try:

    file = open("danezadanie98.txt", "r")

except IOError:
    print("Blad otwierania pliku")

lines = file.readlines()

a = int(lines[0])
b = int(lines[1])
c = int(lines[2])

delta = (b**2) - (4*a*c)

result1 = (-b-cmath.sqrt(delta))/(2*a)
result2 = (-b+cmath.sqrt(delta))/(2*a)

print('Rozwiązania: {0} oraz {1}'.format(result1, result2))

file.close()