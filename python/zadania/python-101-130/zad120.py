from fractions import Fraction

def getNumber(prompt):

    while(True):

        value = input(prompt)

        try:
            n = float(value)
            return n

        except ValueError:
            print("Blad!")

print("out: " + str(Fraction(getNumber("in: ")).limit_denominator()))