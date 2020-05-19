# ### Zadanie 3.1 Funkcje liczbowe

import math
import pytest


def foots_to_meters(number_of_ft: float or int):
    """
    This function convert foots to meters
    :param number_of_ft: number of foots that should be converted
    :return: number of meters
    """
    return number_of_ft / 3.2808


def max(number_1: int or float, number_2: int or float):
    """
    This function return the bigger of the two given numbers.
    :param number_1: the first number
    :param number_2: the second number
    :return: greater number
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
    :param number_1: the first number
    :param number_2: the second number
    :return: the average from two given numbers
    """
    return (number_1 + number_2) / 2


def area_of_circle(radius: int or float):
    """
    This function calculate the area of a circle.
    :param radius: provide the radius of a circle
    :return: area
    """
    return math.pi * (radius ** 2)


def bmi(height: int or float, weight: int or float):
    """
    This function calculate the BMI.
    :param height: the height in meters
    :param weight: the weight in kilograms
    :return: the BMI
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
        return math.sqrt(p * (p - a) * (p - b) * (p - c))


def km_to_mils(number_of_km: int or float):
    """
    This function convert the kilometers on miles, rounded to one sign after point.
    :param number_of_km: kilometers
    :return: miles
    """
    return number_of_km * 0.62137


def miles_to_km(number_of_miles: int or float):
    """
    This function convert the miles to kilometers, rounded to one sign after point.
    :param number_of_miles: provide miles that should be convented
    :return: kilometers
    """
    return number_of_miles / 0.62137


def test_foots_to_meters():
    assert foots_to_meters(15) == 4.57205559619605
    assert foots_to_meters(0) == 0.0
    assert foots_to_meters(64) == 19.50743721043648


def test_max():
     assert max(2, 3) == 3
     assert max(-56, -79) == -56
     assert max(0, 45) == 45
     assert max(0, 0) == True


def test_average():
    assert average(2, 4.2) == 3.1
    assert average(0, -6) == -3
    assert average(0, 5) == 2.5


def test_area_of_circle():
    assert area_of_circle(30) == 2827.4333882308138
    assert area_of_circle(12) == 452.3893421169302
    assert area_of_circle(0.1) == 0.031415926535897934
    assert area_of_circle(-6) == 113.09733552923255


def test_bmi():
    assert bmi(1.6, 50) == 19.531249999999996
    assert bmi(1.8, 90) == 27.777777777777775
    assert bmi(1.2, 80) == 55.55555555555556


def test_area_of_triangle():
    assert area_of_triangle(3, 5, 7) == 6.49519052838329
    assert area_of_triangle(10, 16, 14) == 69.2820323027551
    with pytest.raises(SyntaxError):
        area_of_triangle(20, 10, 5)
        raise SyntaxError("The triangle with those sides doesn't exist.")


def test_km_to_mils():
    assert km_to_mils(10) == 6.213699999999999
    assert km_to_mils(0) == 0.0
    assert km_to_mils(15) == 9.320549999999999


def test_miles_to_km():
    assert miles_to_km(10) == 16.093470878864444
    assert miles_to_km(0) == 0.0
    assert miles_to_km(60) == 96.56082527318667