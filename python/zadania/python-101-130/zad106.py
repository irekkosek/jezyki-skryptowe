import random
import time
import datetime

def bubbleSort(input):
    new = input

    for i in range(0, len(new) - 1):
        for j in range(0, len(new) - 1):
            if new[j] > new[j + 1]:
                new[j], new[j+1] = new[j+1], new[j]

    return new

def insertionSort(input):
    new = input

    for j in range(2, len(new)):
        key = new[j]
        i = j-1
        while i >= 0 and new[i] > key:
            new[i+1] = new[i]
            i -= 1
        new[i+1] = key

    return  new

def quickSort(input):

    def partition(input, p, k):
        x = input[k]
        i = p - 1

        for j in range(p, k):
            if input[j] <= x:
                i += 1
                input[i], input[j] = input[j], input[i]

        input[k], input[i + 1] = input[i + 1], input[k]

        return i + 1

    def main(input, p, k):
        if p < k:
            q = partition(input, p, k)
            main(input, p, q - 1)
            main(input, q + 1, k)

    new = input
    main(new, 0, len(new) - 1)

    return new


numbers = []

for i in range(900):
    numbers.append(random.randint(1, 100))

def writeToFile(i, name, count, time):
    file.write(str(i) + ". " + str(name).ljust(20) + str(count).ljust(30) + str(str(time) + " ms").ljust(30) + "\n")

try:

    file = open("raport_" + str(datetime.date.today()) +  ".txt", "w")

    file.write("RAPORT ALGORYTMOW SORTOWANIA\n\n")
    file.write("NAZWA".ljust(23) + "LICZBA SORTOWANYCH PLIKOW".ljust(30) + "SREDNI CZAS".ljust(30) + "\n")

    startTime = time.time()
    sorted = bubbleSort(numbers)
    stopTime = time.time()
    result = (stopTime - startTime) * 1000
    writeToFile(1, "bąbelkowe", len(numbers), result)

    startTime = time.time()
    sorted = insertionSort(numbers)
    stopTime = time.time()
    result = (stopTime - startTime) * 1000
    writeToFile(2, "wstawianie", len(numbers), result)

    startTime = time.time()
    sorted = quickSort(numbers)
    stopTime = time.time()
    result = (stopTime - startTime) * 1000
    writeToFile(3, "quick sort", len(numbers), result)

    file.close()

except IOError:
    print("Blad otwierania pliku")
