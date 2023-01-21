string = input("Podaj ciag do sprawdzenia: ")

if string == string[::-1]:
    print("Tak, to jest palindrom")
else:
    print("Nie, to nie jest palindrom")