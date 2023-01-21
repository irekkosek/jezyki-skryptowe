import re

try:
    inputFile = open("danezadanie95.txt", "r")
    fileContents = inputFile.read()
    inputFile.close()
except IOError:
    print("Blad otwierania pliku")
    exit()

usedWords = []
times = []

for word in re.sub("[^\w]", " ",  str(fileContents)).split():

    if word not in usedWords:
        usedWords.append(word)
        times.append(1)
    else:
        times[usedWords.index(word)] += 1

for i in range(len(usedWords)):

    print("{:<20}".format(usedWords[i]) + " -  " + str(times[i]))

