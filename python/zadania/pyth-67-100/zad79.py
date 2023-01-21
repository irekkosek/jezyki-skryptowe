alphabet = input("Podaj alfabet: ")

output = []

for letter in alphabet:
    if letter in "aeyioąęuó":
        if letter not in output:
            output.append(letter)

for letter in output:
    print(letter)