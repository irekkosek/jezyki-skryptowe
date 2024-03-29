import math

class ComplexNumber(object):

    def __init__(self, real, imag=0.0):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return ComplexNumber(self.real + other.real,
                       self.imag + other.imag)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real,
                       self.imag - other.imag)

    def __mul__(self, other):
        return ComplexNumber(self.real*other.real - self.imag*other.imag,
                       self.imag*other.real + self.real*other.imag)

    def __truediv__(self, other):
        r = float(other.real**2 + other.imag**2)
        return ComplexNumber((self.real*other.real+self.imag*other.imag)/r, (self.imag*other.imag-self.real*other.imag)/r)

    def __abs__(self):
        return math.sqrt(self.real**2 + self.imag**2)

    def __str__(self):
        if self.imag >= 0:
            return '(%g+%gi)' % (self.real, self.imag)
        return '(%g%gi)' % (self.real, self.imag)

print((-23+0j) / (17+9j))
print(ComplexNumber(-23, 0) / ComplexNumber(17, 9))