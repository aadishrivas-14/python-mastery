"""
Day 1: Python Basics - 20 Exercises
Implement all functions below based on test requirements
"""

# BASIC OPERATIONS (5)

def hello_world():
    """Return the string 'Hello, World!'"""
    return 'Hello, World!'
    pass


def add_numbers(a, b):
    """Add two numbers and return the result"""
    # TODO: Return a + b
    return a + b
    pass


def is_even(n):
    """Check if a number is even"""
    # TODO: Return True if n is even, False otherwise
    # Hint: Use modulo operator %
    return n % 2 == 0
    pass


def max_of_three(a, b, c):
    """Return the maximum of three numbers"""
    # TODO: Return the largest of a, b, c
    # Hint: Use max() function or if statements
    return max(a, b, c)
    pass


def celsius_to_fahrenheit(c):
    """Convert Celsius to Fahrenheit"""
    # TODO: Formula: F = (C * 9/5) + 32
    return (c * 9 / 5) + 32
    pass


# STRING OPERATIONS (5)

def reverse_string(s):
    """Reverse a string"""
    # TODO: Return reversed string
    # Hint: Use slicing s[::-1] or reversed()
    return s[::-1]
    pass


def is_palindrome(s):
    """Check if string is a palindrome (reads same forwards and backwards)"""
    # TODO: Return True if palindrome, False otherwise
    # Hint: Compare string with its reverse
    return s == s[::-1]
    pass


def count_vowels(s):
    """Count number of vowels (a, e, i, o, u) in string"""
    # TODO: Count vowels (case-insensitive)
    # Hint: Loop through string and check if char in 'aeiouAEIOU'
    return sum(1 for char in s if char in 'aeiouAEIOU')
    pass


def capitalize_words(s):
    """Capitalize the first letter of each word"""
    # TODO: Capitalize each word
    # Hint: Use .title() method or split/join
    return ' '.join(word.title() for word in s.split())
    pass


def remove_whitespace(s):
    """Remove all whitespace from string"""
    # TODO: Remove spaces, tabs, newlines
    # Hint: Use .replace() or ''.join()
    return s.replace(' ', '').replace('\t', '').replace('\n', '')
    pass


# NUMBER OPERATIONS (5)

def is_prime(n):
    """Check if number is prime"""
    # TODO: Return True if n is prime, False otherwise
    # Hint: Check divisibility from 2 to sqrt(n)
    return n > 1 and all (n % i != 0 for i in range(2, int(n**0.5) + 1))
    pass


def factorial(n):
    """Calculate factorial of n (n!)"""
    # TODO: Return n! = n * (n-1) * (n-2) * ... * 1
    # Hint: Use loop or recursion
    return 1 if n == 0 else n * factorial(n - 1)
    pass


def fibonacci(n):
    """Return the nth Fibonacci number (0-indexed)"""
    # TODO: Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, ...
    # Hint: fib(n) = fib(n-1) + fib(n-2), base cases: fib(0)=0, fib(1)=1
    return 0 if n == 0 else 1 if n == 1 else fibonacci(n - 1) + fibonacci(n - 2)
    pass

## explain here what str does. 
def sum_of_digits(n):
    """Sum all digits in a number"""
    # TODO: Sum all digits (e.g., 123 -> 1+2+3 = 6)
    # Hint: Convert to string and iterate, or use modulo
    return sum(int(digit) for digit in str(n))
    pass

def gcd(a, b):
    """Calculate Greatest Common Divisor using Euclidean algorithm"""
    # TODO: Return GCD of a and b
    # Hint: Use Euclidean algorithm or math.gcd()
    return a if b == 0 else gcd(b, a % b)
    pass


# LIST OPERATIONS (5)

def find_max(lst):
    """Find maximum element in list"""
    # TODO: Return maximum element
    # Hint: Use max() or loop through list
    return max(lst)
    pass

## set will have only unique elements
def remove_duplicates(lst):
    """Remove duplicate elements from list"""
    # TODO: Return list with unique elements (preserve order)
    # Hint: Use set or loop with checking
    return list(set(lst))
    pass


def flatten_list(lst):
    """Flatten a nested list one level deep"""
    # TODO: [[1,2], [3,4]] -> [1,2,3,4]
    # Hint: Use nested loop or list comprehension
    return [item for sublist in lst for item in sublist]
    pass


def list_intersection(lst1, lst2):
    """Find common elements between two lists"""
    # TODO: Return list of elements in both lists
    # Hint: Use set intersection or loop
    return list(set(lst1) & set(lst2))
    pass


def fizzbuzz(n):
    """Return FizzBuzz list from 1 to n"""
    # TODO: For multiples of 3: "Fizz", 5: "Buzz", both: "FizzBuzz", else: number
    # Hint: Check divisibility by 15, then 3, then 5
    result = []
    pass
