from typing import List
import math


def FizzBuzz(number: int):
    if number % 5 == 0 and number % 3 == 0:
        return("FizzBuzz")
    if number % 3 == 0:
        return("Fizz")
    if number % 5 == 0:
        return("Buzz")
    else:
        return(number)


def FizzBuzz2(number: int):
    word = ""
    if number % 3 == 0:
        word += "Fizz"
    if number % 5 == 0:
        word += "Buzz"

    word = number if word == "" else word
    return word


def FizzBuzz3(number: int):
    word = ""
    word += "Fizz" if number % 3 == 0 else ""
    word += "Buzz" if number % 5 == 0 else ""

    word = number if word == "" else word
    return word




def find_median(numbers : list) :
    numbers = list(numbers)
    isEven = len(numbers) % 2 == 0

    if not isEven :
        z = math.ceil(len(numbers) / 2)
        return numbers[z - 1]
    else :
        number1 = numbers[ int((len(numbers) / 2) - 1)]
        number2 = int(numbers[ int((len(numbers) / 2))])
        return (number1 + number2) / 2


x = find_median((1, 2, 3, 4, 7))
print(x)