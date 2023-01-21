import math
import sys

class Algorithm():
    def solution(self, n):
        sum = math.sqrt(n + 1)
        print("numeric sum: {0}".format(sum))
        print("symbolic sum: sqrt({0})".format(n + 1))

if __name__ == "__main__":
    try:
        n = int(input("Enter n:"))
        if n < 1:
            raise Exception("n must be greater than 0")
    except ValueError:
        print("n must be a number")
        sys.exit(1)
    except Exception as e:
        print(e)
        sys.exit(1)

    calculate = Algorithm()
    calculate.solution(n)
