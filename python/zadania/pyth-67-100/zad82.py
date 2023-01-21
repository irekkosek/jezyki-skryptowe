numbers = []

try:
    file = open("zad081.txt", "r")

    for line in file:
        numbers.append(int(line))

    file.close()

except IOError:
    print("Blad otwierania pliku")

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