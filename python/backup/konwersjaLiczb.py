"""A function that reads numbers from a file and converts them to hex, octal and binary. The results are saved in a new file."""
def convertNumbers(file):
    with open(file, 'r') as f:
        lines = f.read().splitlines()
        for line in lines:
            """Check the number system of the number and convert it to decimal."""
            if line.startswith("0b"):
                number = int(line, 2)
            elif line.startswith("0o"):
                number = int(line, 8)
            elif line.startswith("0x"):
                number = int(line, 16)
            else:
                number = int(line)
            try:
                number = int(line)
                print(f"{number} = {hex(number)} = {oct(number)} = {bin(number)}")
            except ValueError:
                print(f"{line} is not a number.")