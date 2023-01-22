# jan kowalski:10.01.1978:Gliwice:Polska:10.01.2018:Katowice:Polska
# anna kowalski:10.01.1978:Gliwice:Polska:10.01.2018:Gliwice:Polska
# wczytaj z pliku osobe jej wiek oraz plec
# i zapisz do pliku analizadanych.txt w formacie:
# osoba: wiek: plec
#w kolejności malejącej względem wieku oraz płci

import sys

def divide_text(text):
    return text.split(":")

def calculate_age(birth_date, current_date):
    birth_date = birth_date.split(".")
    current_date = current_date.split(".")
    age = int(current_date[2]) - int(birth_date[2])
    if int(current_date[1]) < int(birth_date[1]):
        age -= 1
    elif int(current_date[1]) == int(birth_date[1]) and int(current_date[0]) < int(birth_date[0]):
        age -= 1
    return age


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        for line in file:
            data = divide_text(line)
            age = calculate_age(data[1], data[4])
            with open("analizadanych.txt", "a") as file:
                file.write(data[0] + " " + str(age) + " " + data[2] + "\n")

