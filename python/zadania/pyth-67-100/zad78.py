print("Program pobierze kolejne elementy listy, aby zakonczyc napisz 'end'")

i = 0

myList = []

while(True):

    item = input("Wprowadz element " + str(i+1) + " listy: ")

    if item == "end":
        break

    myList.append(item)
    i += 1

print("\nWprowadzone elementy: ")

for item in myList:
    print(item)