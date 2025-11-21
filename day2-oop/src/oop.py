"""Day 3: Object-Oriented Programming - 15 Exercises"""

# BASIC CLASSES (5)
class Person:
    """TODO: Create Person class with name and age attributes
    Hint: Use __init__ to initialize attributes"""
    def __init__(self, name, age):
        self.name = name
        self.age = age
    pass

class BankAccount:
    """TODO: Create BankAccount with balance, deposit, withdraw methods
    Hint: withdraw should return False if insufficient funds"""
    def __init__(self,balance):
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
            if amount > self.balance:
                return False
            self.balance -= amount
            return True
    pass

class Rectangle:
    """TODO: Create Rectangle with width, height, area, perimeter methods
    Hint: area = w*h, perimeter = 2*(w+h)"""
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height    
    def perimeter(self):
        return 2 * (self.width + self.height)
    pass

class Student:
    """TODO: Create Student with name, grades list, average method
    Hint: Add add_grade method to append to grades list"""
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
    def add_grade(self, grade):
        self.grades.append(grade)
    def average(self):
        return sum(self.grades)/len(self.grades)
    pass

class Counter:
    """TODO: Create Counter with increment, decrement, reset methods
    Hint: Initialize value to 0"""
    def __init__(self):
        self.value = 0
    def increment(self):
        self.value += 1
    def decrement(self):
        self.value -= 1
    def reset(self):
        self.value = 0
    pass

# INHERITANCE (5)
class Animal:
    """TODO: Base class with name and speak method
    Hint: speak returns 'Some sound'"""
    def __init__(self, name):
        self.name = name
    def speak(self):
        return "Some sound"
    pass

class Dog(Animal):
    """TODO: Dog that speaks 'Woof!'
    Hint: Override speak method"""
    def speak(self):
        return "Woof!"
    pass

class Cat(Animal):
    """TODO: Cat that speaks 'Meow!'
    Hint: Override speak method"""
    def speak(self):
        return "Meow!"
    pass

class Vehicle:
    """TODO: Base class with brand, model, start method
    Hint: start returns string with brand and model"""
    def __init__(self, brand, model):
        self.brand = brand
        self.model= model
    def start(self):
        return self.brand +" " + self.model
    pass

class Car(Vehicle):
    """TODO: Car with additional doors attribute
    Hint: Call super().__init__ for brand and model"""
    def __int__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors
    pass

# MAGIC METHODS (5)
class Vector:
    #very nice, this is magic method.
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    pass

class Book:
    """TODO: Book with __eq__, __lt__ for comparison
    Hint: Compare by title and pages"""
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
    def __eq__(self, other):
        return self.pages == other.pages
    def __lt__(self, other):
        return self.pages < other.pages
    pass

class Stack:
    """
    Magic Methods Explained:

    __len__: Called when len(obj) is used
    __bool__: Called when bool(obj) or if obj: is used
    __iter__: Called when list(obj) or for x in obj: is used

    Python's built-in functions automatically call these methods!
    """
    def __init__(self):
        self.items = []

    def __len__(self):
        # len(s) → Python calls this
        return len(self.items)

    def __bool__(self):
        # bool(s) or if s: → Python calls this
        return len(self.items) > 0

    def __iter__(self):
        # list(s) or for x in s: → Python calls this
        return iter(self.items)

class Temperature:
    """
    Property Decorator Explained:

    @property: Makes a method act like an attribute (getter)
    @name.setter: Allows setting the attribute (setter)

    Without @property:
        t.get_celsius()  # Method call

    With @property:
        t.celsius  # Looks like attribute, but runs method!
    """
    def __init__(self, celsius):
        self._celsius = celsius  # _ means "internal/private"

    @property  # Decorator: makes celsius readable
    def celsius(self):
        return self._celsius

    @celsius.setter  # Decorator: makes celsius writable
    def celsius(self, value):
        self._celsius = value
    pass

class Singleton:
    """
    Singleton Pattern: Ensures only ONE instance of the class exists

    __new__ vs __init__:
    - __new__: Creates the object (called first)
    - __init__: Initializes the object (called after __new__)

    How it works:
    1. First call: _instance is None → create new object
    2. Second call: _instance exists → return same object
    3. All calls return the SAME object
    """

    _instance = None  # Class variable (shared across all instances)

    def __new__(cls):
        """
        __new__ is called when you do Singleton()
        It's responsible for creating the actual object
        """
        if cls._instance is None:
            # First time: create new instance
            cls._instance = super().__new__(cls)

        # Always return the same instance
        return cls._instance
    pass
