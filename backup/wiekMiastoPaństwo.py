
"""Divide text into list of strings"""

def divide_text(text):
    return text.split(":")

"""Calculate age"""

def calculate_age(birth_date, current_date):
    birth_date = birth_date.split(".")
    current_date = current_date.split(".")
    age = int(current_date[2]) - int(birth_date[2])
    if int(current_date[1]) < int(birth_date[1]):
        age -= 1
    elif int(current_date[1]) == int(birth_date[1]) and int(current_date[0]) < int(birth_date[0]):
        age -= 1
    return age

"""Check if city is the same"""

def check_city(city1, city2):
    if city1 == city2:
        return True
    else:
        return False

"""Check if country is the same"""

def check_country(country1, country2):
    if country1 == country2:
        return True
    else:
        return False

if __name__ == "__main__":

    with open("input.txt", "r") as file:
        for line in file:
            data = divide_text(line)
            age = calculate_age(data[1], data[4])
            city = check_city(data[2], data[5])
            country = check_country(data[3], data[6])
            """Write name, age, city and country to file"""

            with open("output.txt", "a") as file:
                file.write(data[0] + str(age) + " " + str(city) + " " + str(country) + "\n")