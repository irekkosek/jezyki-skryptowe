myList1 = ["17", 17, "test", 6, 8]
myList2 = ["17", 17, "testujemy", 6]

item = 17

for l in [myList1, myList2]:
    if item in l:
        print("Element " + str(item) + " zawiera sie w liscie", l)
        exit()

print("Element " + str(item) + " nie zawiera sie w zadnej liscie.")