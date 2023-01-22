import sys
import numpy as np

def multiply_matrices(matrices):
    result = matrices[0]
    for i in range(1, len(matrices)):
        result = [[sum(a*b for a, b in zip(X_row, Y_col)) for Y_col in zip(*matrices[i])] for X_row in result]
    return result

def read_matrix(filename):
    with open(filename) as f:
        return np.array([[int(num) for num in line.split()] for line in f])
        
def main():
    matrices = [read_matrix(filename) for filename in sys.argv[1:]]
    print(np.matrix(multiply_matrices(matrices)))

if __name__ == '__main__':
    main()  