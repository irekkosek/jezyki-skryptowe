try:
    inputFile = open("danezadanie91.txt", "r")
    fileContents = inputFile.read()
    inputFile.close()
except IOError:
    print("Blad otwierania pliku")
    exit()

try:
    outputFile = open("wynikzadanie91.txt", "w")
except IOError:
    print("Blad otwierania pliku")
    exit()

try:
    n = int(fileContents)
except ValueError:
    print("Blad!")

outputFile.write(str(n) + "\n")
outputFile.write(str(hex(n)) + "\n")
outputFile.write(str(oct(n)) + "\n")
outputFile.close()