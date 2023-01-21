print("Program pobierze kolejne liczby, aby zakonczyc napisz 'end'")

while(True):

    item = input("Wprowadz liczbe: ")

    if item == "end":
        break

    try:
        value = int(item)
    except ValueError:
        print("Blad!")

