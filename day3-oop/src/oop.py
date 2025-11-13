"""Day 3: Object-Oriented Programming - 15 Exercises"""

# BASIC CLASSES (5)
class Person:
    """TODO: Create Person class with name and age attributes
    Hint: Use __init__ to initialize attributes"""
    pass

class BankAccount:
    """TODO: Create BankAccount with balance, deposit, withdraw methods
    Hint: withdraw should return False if insufficient funds"""
    pass

class Rectangle:
    """TODO: Create Rectangle with width, height, area, perimeter methods
    Hint: area = w*h, perimeter = 2*(w+h)"""
    pass

class Student:
    """TODO: Create Student with name, grades list, average method
    Hint: Add add_grade method to append to grades list"""
    pass

class Counter:
    """TODO: Create Counter with increment, decrement, reset methods
    Hint: Initialize value to 0"""
    pass

# INHERITANCE (5)
class Animal:
    """TODO: Base class with name and speak method
    Hint: speak returns 'Some sound'"""
    pass

class Dog(Animal):
    """TODO: Dog that speaks 'Woof!'
    Hint: Override speak method"""
    pass

class Cat(Animal):
    """TODO: Cat that speaks 'Meow!'
    Hint: Override speak method"""
    pass

class Vehicle:
    """TODO: Base class with brand, model, start method
    Hint: start returns string with brand and model"""
    pass

class Car(Vehicle):
    """TODO: Car with additional doors attribute
    Hint: Call super().__init__ for brand and model"""
    pass

# MAGIC METHODS (5)
class Vector:
    """TODO: Vector class with __add__, __sub__, __mul__, __str__
    Hint: Store x, y; __mul__ is scalar multiplication"""
    pass

class Book:
    """TODO: Book with __eq__, __lt__ for comparison
    Hint: Compare by title and pages"""
    pass

class Stack:
    """TODO: Stack with __len__, __bool__, __iter__
    Hint: Use list internally, push/pop methods"""
    pass

class Temperature:
    """TODO: Temperature with property decorator for celsius/fahrenheit
    Hint: F = C * 9/5 + 32, C = (F - 32) * 5/9"""
    pass

class Singleton:
    """TODO: Implement Singleton pattern
    Hint: Use __new__ to return same instance"""
    pass
