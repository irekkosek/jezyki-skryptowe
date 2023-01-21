myList1 = ["17", 17, "test", 6, 8]
myList2 = ["17", 17, "testujemy", 6]

maxLen = max(len(myList1), len(myList2))

for i in range(maxLen):

    print("Elementy o indeksie " + str(i) + "  =  ", end="")

    if i < len(myList1) and i < len(myList2):
        if myList1[i] == myList2[i]:
            print("Sa takie same")
            continue

    if i < len(myList1):
        print("Lista 1: " + str(myList1[i]), end="")

    if i < len(myList2):

        if i < len(myList1):
            print(",  ", end="")

        print("Lista 2: " + str(myList2[i]), end="")

    print("")