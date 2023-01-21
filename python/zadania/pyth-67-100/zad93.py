try:
    inputFile = open("danezadanie93.txt", "r")
    fileContents = inputFile.read()
    inputFile.close()
except IOError:
    print("Blad otwierania pliku")
    exit()

usedLetters = []
times = []

for letter in str(fileContents):

    if not letter.isalpha():
        continue

    if letter not in usedLetters:
        usedLetters.append(letter)
        times.append(1)
    else:
        times[usedLetters.index(letter)] += 1

for i in range(len(usedLetters)):
    print(usedLetters[i] + "  -  " + str(times[i]))

