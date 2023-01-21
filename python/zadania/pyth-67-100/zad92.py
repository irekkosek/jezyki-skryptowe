import math

def getNumber(prompt):

    while(True):

        value = input(prompt)

        try:
            return float(value)
        except ValueError:
            print("Blad!")


#

print("a)")

alpha = getNumber("Podaj alfa (radiany): ")
beta = getNumber("Podaj beta (radiany): ")
resultA = 2*math.sin(1/2*(alpha+beta))*math.cos(1/2*(alpha-beta))
print("wynik = " + str(resultA))

#

print("\nb)")
x = getNumber("Podaj x: ")
n = int(getNumber("Podaj n: "))
resultB = 1

def product(n, a):
    i = 0
    result = 1
    while i < a:
        result = result * (n-i)
        i += 1
    return result

for i in range(1, n + 1):
    resultB += (product(n, i)*x**i)/math.factorial(i)

print("wynik = " + str(resultB))

#

print("\nc)")
a = getNumber("Podaj a: ")
b = getNumber("Podaj b: ")
c = getNumber("Podaj c: ")

delta = math.sqrt(b**2 - 4*a*c)

resultC1 = (-b+delta)*2*a
resultC2 = (-b-delta)*2*a

print("wynik x1 = " + str(resultC1))
print("wynik x2 = " + str(resultC2))

#

print("\nd)")
x = getNumber("Podaj x: ")
resultD = 1

for i in range(1, 20):
    resultD += (x**i)/math.factorial(i)

print("wynik = " + str(resultD))

#

print("\ne)")
x = getNumber("Podaj x: ")
l = getNumber("Podaj l: ")
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

resultE = a[0]

for i in range(10):
    resultE += (a[i]*math.cos(math.pi*i*x/l) + b[i]*math.sin(math.pi*i*x/l))

print(resultE)

