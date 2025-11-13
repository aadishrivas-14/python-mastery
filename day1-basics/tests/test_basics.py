"""
Day 1: Python Basics - Test Suite
20 exercises with comprehensive test cases
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../src'))
from basics import *


# BASIC OPERATIONS TESTS

def test_hello_world():
    assert hello_world() == "Hello, World!"


def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0
    assert add_numbers(100, 200) == 300


def test_is_even():
    assert is_even(2) == True
    assert is_even(3) == False
    assert is_even(0) == True
    assert is_even(-4) == True
    assert is_even(-3) == False


def test_max_of_three():
    assert max_of_three(1, 2, 3) == 3
    assert max_of_three(3, 2, 1) == 3
    assert max_of_three(5, 5, 5) == 5
    assert max_of_three(-1, -2, -3) == -1


def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212
    assert abs(celsius_to_fahrenheit(37) - 98.6) < 0.1


# STRING OPERATIONS TESTS

def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("Python") == "nohtyP"
    assert reverse_string("") == ""
    assert reverse_string("a") == "a"


def test_is_palindrome():
    assert is_palindrome("racecar") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("") == True
    assert is_palindrome("a") == True
    assert is_palindrome("madam") == True


def test_count_vowels():
    assert count_vowels("hello") == 2
    assert count_vowels("Python") == 1
    assert count_vowels("aeiou") == 5
    assert count_vowels("xyz") == 0
    assert count_vowels("HELLO") == 2


def test_capitalize_words():
    assert capitalize_words("hello world") == "Hello World"
    assert capitalize_words("python programming") == "Python Programming"
    assert capitalize_words("a") == "A"


def test_remove_whitespace():
    assert remove_whitespace("hello world") == "helloworld"
    assert remove_whitespace("  a  b  c  ") == "abc"
    assert remove_whitespace("no spaces") == "nospaces"


# NUMBER OPERATIONS TESTS

def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(17) == True
    assert is_prime(1) == False
    assert is_prime(0) == False


def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(3) == 6


def test_fibonacci():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(5) == 5
    assert fibonacci(10) == 55


def test_sum_of_digits():
    assert sum_of_digits(123) == 6
    assert sum_of_digits(0) == 0
    assert sum_of_digits(999) == 27
    assert sum_of_digits(5) == 5


def test_gcd():
    assert gcd(12, 8) == 4
    assert gcd(17, 5) == 1
    assert gcd(100, 50) == 50
    assert gcd(7, 7) == 7


# LIST OPERATIONS TESTS

def test_find_max():
    assert find_max([1, 2, 3, 4, 5]) == 5
    assert find_max([5, 4, 3, 2, 1]) == 5
    assert find_max([-1, -2, -3]) == -1
    assert find_max([42]) == 42


def test_remove_duplicates():
    assert remove_duplicates([1, 2, 2, 3, 3, 3]) == [1, 2, 3]
    assert remove_duplicates([1, 1, 1]) == [1]
    assert remove_duplicates([1, 2, 3]) == [1, 2, 3]


def test_flatten_list():
    assert flatten_list([[1, 2], [3, 4]]) == [1, 2, 3, 4]
    assert flatten_list([[1], [2], [3]]) == [1, 2, 3]
    assert flatten_list([[]]) == []


def test_list_intersection():
    assert set(list_intersection([1, 2, 3], [2, 3, 4])) == {2, 3}
    assert list_intersection([1, 2], [3, 4]) == []
    assert set(list_intersection([1, 1, 2], [1, 2, 2])) == {1, 2}


def test_fizzbuzz():
    result = fizzbuzz(15)
    assert result[0] == 1
    assert result[2] == "Fizz"  # 3
    assert result[4] == "Buzz"  # 5
    assert result[14] == "FizzBuzz"  # 15
    assert len(result) == 15
