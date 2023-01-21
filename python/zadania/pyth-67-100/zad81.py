print("Program pobierze kolejne liczby i poda ich wartosc srednia i mediane, aby zakonczyc napisz 'end'")

numbers = []

while(True):

    item = input("Wprowadz liczbe: ")

    if item == "end":
        break

    try:
        number = int(item)
        numbers.append(number)
    except ValueError:
        print("Blad!")

n = len(numbers)

if n == 0:
    exit()

numbers.sort(key=int)

numbersSum = 0

for number in numbers:
    numbersSum += number

print("\nSrednia: " + str(numbersSum/len(numbers)))

if n % 2 == 0:
    a = n//2
    b = a+1
    median = (numbers[a-1]+numbers[b-1])/2

else:
    median = numbers[n//2 - 1]

print("Mediana: " + str(median))