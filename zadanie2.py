#pobierz liczby z pliku, ropoznaj zapis dziesiętny, szesnastkowy, ósemkowy
#zapisz do pliku w formacie: liczba dziesiętna, liczba ósemkowa, liczba szesnastkowa

    
input="danezadanie1.txt"
output="wyjsciezad2.txt"

with open(input, "r") as f:
    with open(output, "w") as f2:
        f2.write("liczby dziesietne | liczby osemkowe | liczby szesnastkowe\n")
        f2.write("-------------------|------------------|---------------------\n")
        for line in f:
            if line.startswith("0o"):
                number = int(line, 8)
            elif line.startswith("0x"):
                number = int(line, 16)
            else:
                number = int(line)
            try:
                f2.write("{:d}---- | --{:o}-- | ----{:x}\n".format(number, number, number))
            except ValueError:
                print("Błąd")

