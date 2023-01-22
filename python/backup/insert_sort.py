#wczytaj liczby z pliku danewejsciowe.tx posortuj za pomocą funkcji implementującej algorytm sortowania przez wstawianie
# i zapisz do pliku danewyjsciowe.txt

import sys

def insert_sort(list):
    for i in range(1, len(list)):
        j = i
        while j > 0 and list[j] < list[j-1]:
            list[j], list[j-1] = list[j-1], list[j]
            j -= 1
    return list

def main():
    with open("danewejsciowe.txt", "r") as file:
        for line in file:
            print (line)
            list = line.split()
            list = insert_sort(list)
            with open("danewyjsciowe.txt", "a") as file:
                for i in range(len(list)):
                    file.write(list[i] + "\n")

if __name__ == "__main__":
    main()