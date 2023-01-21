def getNumber():

    while(True):

        value = input("Wprowadz liczbe: ")

        try:
            return int(value)
        except ValueError:
            print("Blad!")


print("\nWprowadzona liczba to: ", getNumber())