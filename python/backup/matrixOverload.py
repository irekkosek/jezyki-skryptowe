"""Create class Matrix in which you overload the operators +, - and *"""
class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        if len(self.matrix) == len(other.matrix):
            new_matrix = []
            for i in range(len(self.matrix)):
                new_matrix.append([])
                for j in range(len(self.matrix[i])):
                    new_matrix[i].append(self.matrix[i][j] + other.matrix[i][j])
            return Matrix(new_matrix)
        else:
            raise ValueError("The matrices must be the same size")

    def __sub__(self, other):
        if len(self.matrix) == len(other.matrix):
            new_matrix = []
            for i in range(len(self.matrix)):
                new_matrix.append([])
                for j in range(len(self.matrix[i])):
                    new_matrix[i].append(self.matrix[i][j] - other.matrix[i][j])
            return Matrix(new_matrix)
        else:
            raise ValueError("The matrices must be the same size")

    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            new_matrix = []
            for i in range(len(self.matrix)):
                new_matrix.append([])
                for j in range(len(self.matrix[i])):
                    new_matrix[i].append(self.matrix[i][j] * other)
            return Matrix(new_matrix)
        elif type(other) == Matrix:
            if len(self.matrix[0]) == len(other.matrix):
                new_matrix = []
                for i in range(len(self.matrix)):
                    new_matrix.append([])
                    for j in range(len(other.matrix[0])):
                        new_matrix[i].append(0)
                for i in range(len(self.matrix)):
                    for j in range(len(other.matrix[0])):
                        for k in range(len(other.matrix)):
                            new_matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]
                return Matrix(new_matrix)
            else:
                raise ValueError("The matrices must be the same size")

    def __str__(self):
        new_matrix = ""
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if j == len(self.matrix[i]) - 1:
                    new_matrix += str(self.matrix[i][j])
                else:
                    new_matrix += str(self.matrix[i][j]) + " "
            if i != len(self.matrix) - 1:
                new_matrix += " "
        return new_matrix

    def __repr__(self):
        return "Matrix({})".format(self.matrix)


if __name__ == "__main__":
    Matrix1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    Matrix2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    Matrix3 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    Matrix4 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    Matrix5 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    print(Matrix1 + Matrix2)

    print(Matrix3 - Matrix4)

    print(Matrix5 * 2)

    print(Matrix1 * Matrix2)

    print(Matrix1 * Matrix3) # ValueError: The matrices must be the same size

