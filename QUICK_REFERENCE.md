# Python Quick Reference

Essential Python syntax for beginners.

## Variables
```python
x = 10              # Integer
name = "Python"     # String
price = 19.99       # Float
is_valid = True     # Boolean
```

## Data Types
```python
# Numbers
int_num = 42
float_num = 3.14

# Strings
text = "Hello"
multi = """Multiple
lines"""

# Lists (mutable)
lst = [1, 2, 3, 4]

# Tuples (immutable)
tup = (1, 2, 3)

# Sets (unique elements)
s = {1, 2, 3}

# Dictionaries
d = {"key": "value", "age": 25}
```

## Operators
```python
# Arithmetic
+ - * / // % **

# Comparison
== != < > <= >=

# Logical
and or not

# Membership
in not in
```

## Control Flow
```python
# If statement
if condition:
    # do something
elif other_condition:
    # do something else
else:
    # default action

# For loop
for item in iterable:
    print(item)

# While loop
while condition:
    # do something

# Break and continue
for i in range(10):
    if i == 5:
        break      # Exit loop
    if i == 3:
        continue   # Skip iteration
```

## Functions
```python
def function_name(param1, param2):
    """Docstring"""
    result = param1 + param2
    return result

# Call function
value = function_name(10, 20)

# Default parameters
def greet(name="World"):
    return f"Hello, {name}!"

# Multiple returns
def min_max(lst):
    return min(lst), max(lst)
```

## Lists
```python
lst = [1, 2, 3, 4, 5]

# Access
lst[0]        # First element
lst[-1]       # Last element
lst[1:3]      # Slice [2, 3]

# Methods
lst.append(6)
lst.insert(0, 0)
lst.remove(3)
lst.pop()
lst.sort()
lst.reverse()

# List comprehension
squares = [x**2 for x in range(10)]
evens = [x for x in range(10) if x % 2 == 0]
```

## Dictionaries
```python
d = {"name": "Alice", "age": 25}

# Access
d["name"]
d.get("age")

# Methods
d.keys()
d.values()
d.items()
d.update({"city": "NYC"})

# Dict comprehension
squares = {x: x**2 for x in range(5)}
```

## Strings
```python
s = "Hello, World!"

# Methods
s.lower()
s.upper()
s.strip()
s.split(",")
s.replace("Hello", "Hi")
s.startswith("Hello")
s.endswith("!")

# Formatting
name = "Alice"
age = 25
f"My name is {name} and I'm {age}"
"My name is {} and I'm {}".format(name, age)

# Slicing
s[0:5]    # "Hello"
s[::-1]   # Reverse
```

## Common Built-in Functions
```python
len(lst)          # Length
max(lst)          # Maximum
min(lst)          # Minimum
sum(lst)          # Sum
sorted(lst)       # Sorted copy
range(10)         # 0 to 9
enumerate(lst)    # Index, value pairs
zip(lst1, lst2)   # Combine lists
map(func, lst)    # Apply function
filter(func, lst) # Filter elements
```

## File I/O
```python
# Read
with open("file.txt", "r") as f:
    content = f.read()
    lines = f.readlines()

# Write
with open("file.txt", "w") as f:
    f.write("Hello\n")
    f.writelines(["Line 1\n", "Line 2\n"])

# Append
with open("file.txt", "a") as f:
    f.write("More text\n")
```

## Exception Handling
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
except Exception as e:
    print(f"Error: {e}")
finally:
    print("Always executes")
```

## Classes
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        return f"Hi, I'm {self.name}"

# Create object
p = Person("Alice", 25)
print(p.greet())
```

## Lambda Functions
```python
# Anonymous function
square = lambda x: x**2
add = lambda x, y: x + y

# With map/filter
squares = list(map(lambda x: x**2, [1,2,3]))
evens = list(filter(lambda x: x % 2 == 0, [1,2,3,4]))
```

## Useful Patterns
```python
# Swap variables
a, b = b, a

# Multiple assignment
x, y, z = 1, 2, 3

# Unpacking
first, *rest = [1, 2, 3, 4]

# Ternary operator
result = "even" if x % 2 == 0 else "odd"

# Check existence
if item in lst:
    print("Found")

# Iterate with index
for i, value in enumerate(lst):
    print(f"{i}: {value}")
```

## Testing with pytest
```python
# test_example.py
def test_addition():
    assert 1 + 1 == 2

def test_string():
    assert "hello".upper() == "HELLO"

# Run tests
# python3 -m pytest test_example.py -v
```

## Common Mistakes to Avoid
```python
# ❌ Mutable default argument
def bad(lst=[]):
    lst.append(1)
    return lst

# ✅ Use None
def good(lst=None):
    if lst is None:
        lst = []
    lst.append(1)
    return lst

# ❌ Modifying list while iterating
for item in lst:
    lst.remove(item)  # Bad!

# ✅ Use list copy
for item in lst[:]:
    lst.remove(item)  # Good
```

## Debugging
```python
# Print debugging
print(f"Value: {variable}")

# Type checking
print(type(variable))

# Dir (see methods)
print(dir(object))

# Help
help(function_name)
```

---

**Keep this reference handy while working through exercises!** 🐍
