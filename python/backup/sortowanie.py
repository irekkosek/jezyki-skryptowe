class Sortowanie:
    def babelkowe(self, lista):
        for i in range(len(lista)):
            for j in range(len(lista) - 1):
                if lista[j] > lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
        return lista
    
    def Shell(self, lista):
        n = len(lista)
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                temp = lista[i]
                j = i
                while j >= gap and lista[j - gap] > temp:
                    lista[j] = lista[j - gap]
                    j -= gap
                lista[j] = temp
            gap //= 2
        return lista

def read(filename):
    with open(filename) as file:
        return [int(line) for line in file]

def write(filename, lista):
    with open(filename, "w") as file:
        for i in range(len(lista)):
            file.write(str(lista[i]) + "\n")

lista1=read("tosort1.txt")
lista2=read("tosort2.txt")
Sortowanie = Sortowanie()
Sortowanie.babelkowe(lista1)
Sortowanie.Shell(lista2)
write("tosort1.txt", lista1)
write("tosort2.txt", lista2)

