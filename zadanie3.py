input="macierzwejsciowa.txt"
output="macierzwynikowa.txt"

with open(input, "r") as f:
    with open(output, "w") as f2:
        for line in f:
            f2.write(line)

def transpose(matrix):
    return list(map(list, zip(*matrix)))

with open(input, "r") as f:
    with open(output, "w") as f2:
        matrix = [[int(x) for x in line.split()] for line in f]
        matrix = transpose(matrix)
        for line in matrix:
            f2.write(" ".join([str(x) for x in line]) + "\n")