import calendar

def getNumber(prompt):

    while(True):

        value = input(prompt)

        try:
            return int(value)
        except ValueError:
            print("Blad!")


a = getNumber("Podaj rok o ktorego chcesz rozpoczac sprawdzanie: ")
b = getNumber("Podaj rok na ktorych chcesz zakonczyc sprawdzanie: ")

for year in range(min(a, b), max(a,b)):
    if calendar.isleap(year):
        print("Rok " + str(year) + " jest przestepny.")