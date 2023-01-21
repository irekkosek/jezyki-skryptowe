
class Matma:
    staticmethod
    def pow(self, x, n):
        if x == 0 or x == 1 or n == 1:
            return x
        result = 1
        for _ in range(n):
            result *= x
        return result

matma = Matma()

print(matma.pow(2,8))