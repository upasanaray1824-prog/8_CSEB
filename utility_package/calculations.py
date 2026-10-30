"""
Reusable calculation functions for Smart Calculation Utility.
"""

import math
import random

calculation_count = 0


def record_calculation():
    global calculation_count
    calculation_count += 1


def add(a, b):
    record_calculation()
    return a + b


def subtract(a, b):
    record_calculation()
    return a - b


def multiply(a, b):
    record_calculation()
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    record_calculation()
    return a / b


def percentage(number, percent=10):
    record_calculation()
    return number * percent / 100


def square_root(number):
    if number < 0:
        raise ValueError("Square root of a negative number is not supported.")
    record_calculation()
    return math.sqrt(number)


def power(base, exponent=2):
    record_calculation()
    return math.pow(base, exponent)


def factorial(number):
    if not isinstance(number, int) or number < 0:
        raise ValueError("Factorial requires a non-negative whole number.")
    record_calculation()
    return math.factorial(number)


def random_integer(start, end):
    if start > end:
        raise ValueError("Start must be less than or equal to end.")
    record_calculation()
    return random.randint(start, end)


square = lambda number: number * number


def get_calculation_count():
    return calculation_count
  
