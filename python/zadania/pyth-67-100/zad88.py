import random

def getNumber(prompt):

    while(True):

        value = input(prompt)

        try:
            return int(value)
        except ValueError:
            print("Blad!")

r = getNumber("Podaj liczbe wierszy: ")
c = getNumber("Podaj liczbe kolumn: ")

for i in range(r):
    for j in range(c):
        print("{:<6}".format(str(random.randint(0,100))), end="")
    print("")
