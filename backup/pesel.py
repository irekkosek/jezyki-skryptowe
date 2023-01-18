"""Check if PESEL is valid"""

def checkPesel(pesel):
    """Check if PESEL is valid"""
    if len(pesel) != 11:
        return False
    try:
        int(pesel)
    except ValueError:
        return False
    weights = (1, 3, 7, 9, 1, 3, 7, 9, 1, 3)
    sum = 0
    for i in range(10):
        sum += int(pesel[i]) * weights[i]
    return (10 - sum % 10) % 10 == int(pesel[10])

if __name__ == '__main__':
    pesel = input('Enter PESEL: ')
    if checkPesel(pesel):
        print('PESEL is valid')
    else:
        print('PESEL is invalid')