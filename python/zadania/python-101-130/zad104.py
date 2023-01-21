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

try:

    file = open("danezadanie104.txt", "r")

    for line in file.readlines():
        try:
            numbers.append(int(line))
        except ValueError:
            continue

    file.close()

    ## BUBBLE SORT

    bubbleFile = open("zadanie104_bubble.txt", "w")

    for number in bubbleSort(numbers):
        bubbleFile.write(str(number) + "\n")

    bubbleFile.close()


    ## INSERTION SORT

    insertionFile = open("zadanie104_insertion.txt", "w")

    for number in insertionSort(numbers):
        insertionFile.write(str(number) + "\n")

    insertionFile.close()


    ## QUICK SORT

    quickFile = open("zadanie104_quick.txt", "w")

    for number in quickSort(numbers):
        quickFile.write(str(number) + "\n")

    quickFile.close()

except IOError:
    print("Blad otwierania pliku")