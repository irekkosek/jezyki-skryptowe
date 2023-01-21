i = 0

for gender in ["Mezczyzna", "Kobieta"]:
    for color in ["bialy", "czarny", "zielony", "czerwony", "niebieski"]:
        for size in ["XL", "L", "M", "S"]:
            try:
                outputFile = open("wyjsciezadanie100_metka" + str(i) + ".txt", "w")
                outputFile.write(gender + ", " + color + ", " + size)
                i+=1
            except IOError:
                print("Blad otwierania pliku")
                exit()
            finally:
                outputFile.close()