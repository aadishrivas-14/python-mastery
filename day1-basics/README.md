# Day 1: Python Basics

Master Python fundamentals in one day!

## 📚 Topics Covered

1. Variables and Data Types
2. Operators (arithmetic, comparison, logical)
3. Strings and String Methods
4. Numbers (int, float)
5. Booleans
6. Input/Output
7. Conditionals (if/elif/else)
8. Loops (for, while, break, continue)
9. Functions (def, parameters, return)
10. Lists basics
11. List comprehensions
12. Basic file I/O

## 🎯 Exercises (20)

### Basic Operations (5)
1. `hello_world()` - Return "Hello, World!"
2. `add_numbers(a, b)` - Add two numbers
3. `is_even(n)` - Check if number is even
4. `max_of_three(a, b, c)` - Return maximum of three numbers
5. `celsius_to_fahrenheit(c)` - Convert temperature

### String Operations (5)
6. `reverse_string(s)` - Reverse a string
7. `is_palindrome(s)` - Check if palindrome
8. `count_vowels(s)` - Count vowels in string
9. `capitalize_words(s)` - Capitalize each word
10. `remove_whitespace(s)` - Remove all whitespace

### Number Operations (5)
11. `is_prime(n)` - Check if number is prime
12. `factorial(n)` - Calculate factorial
13. `fibonacci(n)` - Return nth Fibonacci number
14. `sum_of_digits(n)` - Sum all digits
15. `gcd(a, b)` - Greatest common divisor

### List Operations (5)
16. `find_max(lst)` - Find maximum in list
17. `remove_duplicates(lst)` - Remove duplicates
18. `flatten_list(lst)` - Flatten nested list
19. `list_intersection(lst1, lst2)` - Find common elements
20. `fizzbuzz(n)` - Return FizzBuzz list up to n

## 🚀 Getting Started

```bash
# Run all tests
python3 -m pytest tests/ -v

# Run specific test
python3 -m pytest tests/test_basics.py::test_hello_world -v

# Implement in src/basics.py
vim src/basics.py
```

## 💡 Tips

- Start with `hello_world()` - simplest function
- Read test cases to understand requirements
- Use Python's built-in functions
- Google syntax when stuck
- Test frequently

## 📖 Python Syntax Quick Reference

### Variables
```python
x = 10
name = "Python"
is_valid = True
```

### Functions
```python
def function_name(param1, param2):
    result = param1 + param2
    return result
```

### Conditionals
```python
if condition:
    # do something
elif other_condition:
    # do something else
else:
    # default action
```

### Loops
```python
# For loop
for i in range(10):
    print(i)

# While loop
while condition:
    # do something
```

### Lists
```python
lst = [1, 2, 3, 4, 5]
lst.append(6)
lst[0]  # Access first element
```

## ✅ Completion Criteria

- [ ] All 20 tests passing
- [ ] Understand each solution
- [ ] Can explain the code
- [ ] Ready for Day 2!

**Time:** 6-8 hours
