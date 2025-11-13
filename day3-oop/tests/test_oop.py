import sys
sys.path.insert(0, '../src')
from oop import *

def test_person():
    p = Person("Alice", 30)
    assert p.name == "Alice"
    assert p.age == 30

def test_bank_account():
    acc = BankAccount(100)
    acc.deposit(50)
    assert acc.balance == 150
    acc.withdraw(30)
    assert acc.balance == 120
    assert acc.withdraw(200) == False

def test_rectangle():
    r = Rectangle(5, 3)
    assert r.area() == 15
    assert r.perimeter() == 16

def test_student():
    s = Student("Bob", [85, 90, 78])
    assert s.average() == 84.33 or abs(s.average() - 84.33) < 0.01
    s.add_grade(92)
    assert len(s.grades) == 4

def test_counter():
    c = Counter()
    c.increment()
    c.increment()
    assert c.value == 2
    c.decrement()
    assert c.value == 1
    c.reset()
    assert c.value == 0

def test_animal():
    a = Animal("Generic")
    assert a.name == "Generic"
    assert a.speak() == "Some sound"

def test_dog():
    d = Dog("Buddy")
    assert d.name == "Buddy"
    assert d.speak() == "Woof!"

def test_cat():
    c = Cat("Whiskers")
    assert c.name == "Whiskers"
    assert c.speak() == "Meow!"

def test_vehicle():
    v = Vehicle("Toyota", "Camry")
    assert v.brand == "Toyota"
    assert v.model == "Camry"
    assert "Toyota Camry" in v.start()

def test_car():
    c = Car("Honda", "Civic", 4)
    assert c.brand == "Honda"
    assert c.doors == 4
    assert "Honda Civic" in c.start()

def test_vector():
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    v3 = v1 + v2
    assert v3.x == 4 and v3.y == 6
    v4 = v2 - v1
    assert v4.x == 2 and v4.y == 2
    v5 = v1 * 3
    assert v5.x == 3 and v5.y == 6

def test_book():
    b1 = Book("Python", 500)
    b2 = Book("Python", 500)
    b3 = Book("Java", 400)
    assert b1 == b2
    assert b3 < b1

def test_stack():
    s = Stack()
    s.push(1)
    s.push(2)
    assert len(s) == 2
    assert bool(s) == True
    assert s.pop() == 2
    assert list(s) == [1]

def test_temperature():
    t = Temperature(0)
    assert t.celsius == 0
    assert t.fahrenheit == 32
    t.fahrenheit = 212
    assert t.celsius == 100

def test_singleton():
    s1 = Singleton()
    s2 = Singleton()
    assert s1 is s2
