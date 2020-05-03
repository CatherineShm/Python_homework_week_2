# ### Zadanie 3.1 Funkcje liczbowe
#
# Stwórz następujące funkcje. Niech każda z nich przyjmuje w argument do przeliczenia i zwraca przeliczoną wartość.
#
# 1. done `stopy_na_metry` - przelicza odległość wyrażoną w stopach na metry,
# 2. done `max` - zwraca większą z dwóch liczb - postaraj się nie używać funkcji `max` wbudowanej w pythona
# 3. done `srednia` - oblicza średnią z dwóch liczb,
# 4. done `pole_kola` - oblicza pole koła o podanym promieniu (jeden parametr)
# podpowiedź: wartość PI jest dostępna jako `Math.PI`
# 5. done `bmi` - oblicza współczynnik BMI dla podanych dwóch parametrów: wzrostu w metrach i wagi w kg.
# 6. done `pole_trojkata` - z trzema parametrami - oblicza pole trójkąta o podanych bokach z wzoru Herona.
# 7. `kilometry_na_mile` - przelicza odległość wyrażoną w kilometrach na mile
# 8. `mile_na_kilometry` - przelicza odległość wyrażoną w milach na kilometry
#
# Dla wybranych napisz też interaktywne programy, które pytają użytkownika o dane i wypisują wynik.
import math
def foots_to_meters(number_of_ft: float or int):
    """
    This function convert foots to meters
    :param number_of_ft:
    :return: number of meters, rounded to one sign after point.
    """
    return round(number_of_ft / 3.2808, 1)

def max(number_1: int or float, number_2: int or float):
    """
    This function return the bigger of the two given numbers.
    :param number_1:
    :param number_2:
    :return:
    """
    if number_1 < number_2:
        return number_2
    elif number_2 < number_1:
        return number_1
    else:
        return number_1 == number_2
def average(number_1: int or float, number_2: int or float):
    """
    This function calculate the average from two given numbers.
    :param number_1:
    :param number_2:
    :return:
    """
    return (number_1 + number_2) / 2

def erea_of_circle(radius: int or float):
    """
    This function calculate the area of a circle.
    :param radius:
    :return:
    """
    return math.pi * (radius ** 2)

def BMI(height: int or float, weight: int or float):
    """
    This function calculate the BMI.
    :param height: the height in meters
    :param weight: the weight in kilograms
    :return:
    """
    return weight / (height ** 2)

def area_of_triangle(a: int or float, b: int or float, c: int or float):
    """
    This function calculate the area of a triangle calculated by Heron's Formula
    :param a: the first side
    :param b:the second side
    :param c:the third side
    :return: the area of a triangle
    """
    if a + b < c or b + c < a or c + a < b:
        raise SyntaxError("The triangle with those sides doesn't exist.")
    else:
        p = (a + b + c) / 2
        return math.sqrt(p(p - a)(p - b)(p - c))

def km_to_mils(number_of_km: int or float):

    """
    This function convert the kilometers on miles, rounded to one sign after point.
    :param number_of_km:
    :return: miles
    """
    return round(number_of_km * 0.62137, 1)

def miles_to_km(number_of_miles: int or float):
    """
    This function convert the miles to kilometers, rounded to one sign after point.
    :param number_of_miles:
    :return:
    """
    return round(number_of_miles / 0.62137, 1)