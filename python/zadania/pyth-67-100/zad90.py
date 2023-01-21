def getNumber(prompt):

    while(True):

        value = input(prompt)

        try:
            return int(value)
        except ValueError:
            print("Blad!")

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


n = getNumber("Podaj liczbę: ")

print(str(n) + "! = " + str(factorial(n)))