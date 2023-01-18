"""Take a number from file, convert to hex and octal, and write all three numbers to file"""

def main():
    """Main function"""

    input = "dane.txt"
    out = "out.txt"
    with open(input, "r") as input_file:
        with open(out, "w") as output_file:
            for line in input_file:
                number = int(line)
                output_file.write("{:d} {:x} {:o}".format(number, number, number))


if __name__ == "__main__":
    main()
