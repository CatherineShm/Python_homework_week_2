### Zadanie 3.3 | Operacje na listach


def sum(numbers=[]):
    """
    Count the sum of the numbers.
    :param args: numbers
    :return: sum
    """
    sum = 0
    for x in numbers:
        sum += x
    return sum


def average(numbers=[]):
    """
    Count the average of the numbers.
    :param args: numbers
    :return: the average
    """
    sum = 0
    count = 0
    for number in numbers:
        sum += number
        count += 1
    return sum / count


def max(numbers=[]):
    """
    Return the greatest number.
    :param args: numbers
    :return: the greater one
    """
    for num in numbers:
        number = num
        if num > number:
            number = num
    return number


def difference_max_min(numbers=[]):
    """
    This function count the difference between the max and the min numbers.
    :param args: numbers
    :return: the difference between the max and the min
    """
    if numbers == []:
        return 0
    min = numbers[0]
    max = numbers[0]
    for number in numbers:
        if min > number:
            min = number
        if max < number:
            max = number
    return max - min


def greater_than(number: int or float, numbers=[]):
    """
    This return all greater numbers that indicated number.
    :param args: all numbers
    :param number: number
    :return: all greater numbers
    """
    result = []
    for character in numbers:
        if character > number:
            result.append(character)
    return result


def first_greater_than(number: int or float, numbers=[]):
    """
    This return the first greater number that indicated number.
    :param args: all numbers
    :param number: number
    :return: the first greater number
    """
    for character in numbers:
        if character > number:
            return character
    return None


def sum_of_greater(number: int or float, numbers=[]):
    """
    This return the sum of all greater numbers that indicated number.
    :param args: all numbers
    :param number: number
    :return: all greater numbers
    """
    all_greater = []
    for character in numbers:
        if character > number:
            all_greater.append(character)
    result = 0
    for numbers in all_greater:
        result += numbers
    return result


def count_of_greater(number: int or float, numbers=[]):
    """
    This function count all greater numbers that indicated number.
    :param args: all numbers
    :param number: number
    :return: count of greater numbers
    """
    count = 0
    for character in numbers:
        if character > number:
            count += 1
    if count == 0:
        return None
    else:
        return count


def divisible(number: int or float, numbers=[]):
    """
    This function return all numbers that are divisible by the indicated number
    :param args: all numbers
    :param number: indicated number
    :return: numbers from all numbers that are divisible by the indicated number
    """
    if number == 0:
        return "Chcesz dzielić przez zero? Zastanów się."

    all_divisible = []
    for character in numbers:
        if character % number == 0:
            all_divisible.append(character)
    if all_divisible == []:
        return None
    else:
        return all_divisible


def first_divisible(number: int or float, numbers=[]):
    """
    This function return the first number that is divisible by the indicated number
    :param args: all numbers
    :param number: indicated number
    :return: the first number from all numbers that is divisible by the indicated number
    """
    if number == 0:
        return "Chcesz dzielić przez zero? Zastanów się."
    for character in numbers:
        if character % number == 0:
            return character
    return None

def find_joint(numbers1: set, numbers2: set):
    """
    This function return the commune number(s) for two sets of numbers
    :param numbers1: the first set
    :param numbers2: the second set
    :return: the commune element(s)
    """
    result = numbers1 & numbers2
    if result == set():
        return None
    else:
        return result

def test_sum():
    assert sum([5, 10, 1]) == 16
    assert sum([-2, 0, 51]) == 49


def test_average():
    assert average([5, 13]) == 9
    assert average([11, 0, -2]) == 3


def test_max():
    assert max([4, 2, 49]) == 49
    assert max([-50, 0, 60]) == 60


def test_difference_max_min():
    assert difference_max_min([2, 3, 5]) == 3
    assert difference_max_min([-4, 10, 4]) == 14
    assert difference_max_min([]) == 0


def test_greater_than():
    assert greater_than(number=0, numbers=[2, -5, 0, 4]) == [2, 4]
    assert greater_than(number=5, numbers=[-10, 13, 10, 2]) == [13, 10]


def test_first_reater_than():
    assert first_greater_than(numbers=[-10, 13, 10, 2], number=5) == 13
    assert first_greater_than(numbers=[-2, 0, 4, 6], number=2) == 4
    assert first_greater_than(numbers=[0, 2, 5], number= 7) == None


def test_sum_of_greater():
    assert sum_of_greater(numbers=[2, -5, 0, 4], number=0) == 6
    assert sum_of_greater(numbers=[-10, 13, 10, 2], number=5) == 23


def test_count_of_greater():
    assert count_of_greater(numbers=[2, -5, 0, 4], number=0) == 2
    assert count_of_greater(numbers=[-10, 13, 2], number=5) == 1
    assert count_of_greater(numbers=[10, 0, 2], number=12) == None


def test_divisible():
    assert divisible(numbers=[1, 3, 4, 6], number=2) == [4, 6]
    assert divisible(numbers=[-3, 12, 14], number=3) == [-3, 12]
    assert divisible(numbers=[0, 1, 2], number=0) == "Chcesz dzielić przez zero? Zastanów się."
    assert divisible(numbers=[2, 3, 7, 9], number=5) == None


def test_first_divisible():
    assert first_divisible(numbers=[1, 3], number=1) == 1
    assert first_divisible(numbers=[-5, 4, 6, 9], number=3) == 6
    assert first_divisible(numbers=[1, 2, 3], number=0) == "Chcesz dzielić przez zero? Zastanów się."
    assert first_divisible(numbers=[2, 3, 6, 9], number=5) == None


def test_find_joint():
    assert find_joint({1, 2 , 3}, {2, 3, 4}) == {2, 3}
    assert find_joint({2, 5, -10}, {0, -10, 4}) == {-10}
    assert find_joint({8, 6, 7}, {9, 5, 1}) == None