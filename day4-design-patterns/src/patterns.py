"""Day 5: Design Patterns - 15 Exercises"""

# CREATIONAL PATTERNS (4)
class Singleton:
    """TODO: Singleton pattern - only one instance
    Hint: Use __new__ to control instance creation"""
    pass

class ShapeFactory:
    """TODO: Factory pattern - create shapes
    Hint: create_shape(type) returns Circle/Square/Triangle"""
    pass

class PizzaBuilder:
    """TODO: Builder pattern - build pizza step by step
    Hint: Methods: add_cheese(), add_pepperoni(), build()"""
    pass

class Prototype:
    """TODO: Prototype pattern - clone objects
    Hint: Implement clone() method using copy.deepcopy"""
    pass

# STRUCTURAL PATTERNS (4)
class Adapter:
    """TODO: Adapter pattern - adapt interface
    Hint: Wrap incompatible class, translate methods"""
    pass

class LoggerDecorator:
    """TODO: Decorator pattern - add logging
    Hint: Wrap object, add behavior before/after calls"""
    pass

class ComputerFacade:
    """TODO: Facade pattern - simplify complex system
    Hint: start() calls CPU.start(), Memory.load(), HDD.read()"""
    pass

class ImageProxy:
    """TODO: Proxy pattern - lazy loading
    Hint: Load image only when display() is called"""
    pass

# BEHAVIORAL PATTERNS (7)
class Subject:
    """TODO: Observer pattern - notify observers
    Hint: attach(), detach(), notify() methods"""
    pass

class PaymentStrategy:
    """TODO: Strategy pattern - payment methods
    Hint: CreditCard, PayPal, Bitcoin strategies"""
    pass

class Command:
    """TODO: Command pattern - encapsulate actions
    Hint: execute(), undo() methods"""
    pass

class State:
    """TODO: State pattern - state-based behavior
    Hint: Context switches between states"""
    pass

class CustomIterator:
    """TODO: Iterator pattern - custom iteration
    Hint: __iter__() and __next__()"""
    pass

class DataProcessor:
    """TODO: Template Method - algorithm skeleton
    Hint: read(), process(), write() with hook methods"""
    pass

class Handler:
    """TODO: Chain of Responsibility - request chain
    Hint: set_next(), handle() methods"""
    pass
