def encrypt(inputText, shift):

    output = ""

    for ch in inputText.lower():

        if ch.isalpha():
            shiftedChar = ord(ch) + shift
        else:
            output += ' '
            continue

        if shiftedChar > ord('z'):
            shiftedChar -= 26

        output += chr(shiftedChar)

    return output


def decrypte(inputText, shift):

    output = ""

    for c in inputText.lower():

        if c.isalpha():
            shiftedChar = ord(c) - shift
        else:
            output += ' '
            continue

        if shiftedChar > ord('z'):
            shiftedChar += 26

        output += chr(shiftedChar)

    return output


print(encrypt("ala ma kota", 3))
print(decrypte("dod pd nrwd", 3))
