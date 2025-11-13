# Python Mastery in 7 Days - Zero to Hero

Complete Python mastery roadmap: From absolute beginner to advanced patterns and algorithms in one week!

## 📊 Overview

- **Day 1:** Python Basics (20 exercises)
- **Day 2:** Data Structures (20 exercises)
- **Day 3:** Object-Oriented Programming (15 exercises)
- **Day 4:** Advanced Python (15 exercises)
- **Day 5:** Design Patterns (15 exercises)
- **Day 6:** Algorithms & DSA (30 exercises)
- **Day 7:** Real Projects (5 projects)

**Total: 120 exercises + 5 projects**

---

## 🎯 Quick Start

```bash
# Day 1 - Start here!
cd day1-basics
python3 -m pytest tests/ -v

# Implement functions in src/
vim src/basics.py

# Test specific exercise
python3 -m pytest tests/test_basics.py::test_hello_world -v
```

---

## 📅 7-Day Roadmap

### Day 1: Python Basics (20 exercises)
**Topics:**
- Variables, data types, operators
- Strings, numbers, booleans
- Input/output, formatting
- Conditionals (if/elif/else)
- Loops (for, while)
- Functions, parameters, return
- List comprehensions
- Basic file I/O

**Exercises:** Hello World, Calculator, FizzBuzz, Palindrome, Prime Numbers, Fibonacci, String Manipulation, List Operations

**Time:** 6-8 hours

---

### Day 2: Data Structures (20 exercises)
**Topics:**
- Lists (methods, slicing, operations)
- Tuples (immutability, packing/unpacking)
- Sets (operations, methods)
- Dictionaries (CRUD, methods)
- Collections module (Counter, defaultdict, deque)
- List/Dict/Set comprehensions
- Iterators and generators
- Lambda functions

**Exercises:** Array manipulation, Hash maps, Stack, Queue, Deque operations, Set operations, Dictionary problems

**Time:** 6-8 hours

---

### Day 3: Object-Oriented Programming (15 exercises)
**Topics:**
- Classes and objects
- Attributes and methods
- `__init__`, `__str__`, `__repr__`
- Inheritance (single, multiple)
- Polymorphism
- Encapsulation (private, protected)
- Property decorators
- Class methods, static methods
- Abstract classes
- Magic methods (`__add__`, `__len__`, etc.)

**Exercises:** Bank Account, Shape Hierarchy, Animal Classes, Vehicle System, Employee Management

**Time:** 6-8 hours

---

### Day 4: Advanced Python (15 exercises)
**Topics:**
- Decorators (function, class)
- Context managers (`with` statement)
- Generators and yield
- Iterators protocol
- Exception handling (try/except/finally)
- Custom exceptions
- File handling (read, write, modes)
- Regular expressions
- Modules and packages
- `*args` and `**kwargs`

**Exercises:** Custom decorators, Context managers, Generator functions, Exception handling, Regex patterns

**Time:** 6-8 hours

---

### Day 5: Design Patterns (15 exercises)
**Topics:**
- Singleton pattern
- Factory pattern
- Builder pattern
- Observer pattern
- Strategy pattern
- Decorator pattern
- Adapter pattern
- Command pattern
- Template method
- State pattern

**Exercises:** Implement each pattern with real-world examples

**Time:** 6-8 hours

---

### Day 6: Algorithms & DSA (30 exercises)
**Topics:**
- Sorting (bubble, merge, quick, heap)
- Searching (binary, linear)
- Two pointers technique
- Sliding window
- Hash tables
- Linked lists
- Stacks and queues
- Trees (binary, BST)
- Graphs (DFS, BFS)
- Dynamic programming basics
- Recursion and backtracking

**Exercises:** 30 LeetCode-style problems (Easy to Medium)

**Time:** 8-10 hours

---

### Day 7: Real Projects (5 projects)
**Projects:**
1. **CLI Todo App** - CRUD operations, file persistence
2. **Web Scraper** - BeautifulSoup, requests
3. **REST API** - Flask/FastAPI basics
4. **Data Analysis** - Pandas, NumPy basics
5. **Mini Game** - Snake or Tic-Tac-Toe

**Time:** 8-10 hours

---

## 📁 Structure

```
python-mastery/
├── day1-basics/
│   ├── src/basics.py           # TODO: Implement
│   ├── tests/test_basics.py    # 20 tests
│   └── README.md
├── day2-data-structures/
│   ├── src/data_structures.py  # TODO: Implement
│   ├── tests/test_ds.py        # 20 tests
│   └── README.md
├── day3-oop/
│   ├── src/oop.py              # TODO: Implement
│   ├── tests/test_oop.py       # 15 tests
│   └── README.md
├── day4-advanced/
│   ├── src/advanced.py         # TODO: Implement
│   ├── tests/test_advanced.py  # 15 tests
│   └── README.md
├── day5-design-patterns/
│   ├── src/patterns.py         # TODO: Implement
│   ├── tests/test_patterns.py  # 15 tests
│   └── README.md
├── day6-algorithms/
│   ├── src/algorithms.py       # TODO: Implement
│   ├── tests/test_algorithms.py # 30 tests
│   └── README.md
├── day7-projects/
│   ├── todo_app/
│   ├── web_scraper/
│   ├── rest_api/
│   ├── data_analysis/
│   └── mini_game/
└── README.md
```

---

## 🚀 How to Use

### Setup
```bash
# Install Python 3.8+
python3 --version

# Install pytest
pip3 install pytest

# Optional: Create virtual environment
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
```

### TDD Workflow
1. **Read test** - Understand requirements
2. **Run test** - See it fail
3. **Implement** - Write minimal code
4. **Test** - See it pass
5. **Refactor** - Improve code
6. **Repeat** - Next exercise

### Example
```bash
# Day 1
cd day1-basics

# See all tests fail
python3 -m pytest tests/ -v

# Implement first function
vim src/basics.py

# Test specific function
python3 -m pytest tests/test_basics.py::test_hello_world -v

# When it passes, move to next!
```

---

## 📚 Learning Resources

### Official Docs
- [Python.org Tutorial](https://docs.python.org/3/tutorial/)
- [Python Standard Library](https://docs.python.org/3/library/)

### Books (Optional)
- **Automate the Boring Stuff with Python** - Al Sweigart
- **Python Crash Course** - Eric Matthes
- **Fluent Python** - Luciano Ramalho

### Practice
- [LeetCode](https://leetcode.com) - Algorithms
- [HackerRank](https://hackerrank.com) - Python track
- [Real Python](https://realpython.com) - Tutorials

---

## 🎯 Daily Goals

### Day 1: ✅ 20/20 exercises
- Understand Python syntax
- Write basic programs
- Use control flow
- Create functions

### Day 2: ✅ 20/20 exercises
- Master built-in data structures
- Use comprehensions
- Work with collections
- Understand iterators

### Day 3: ✅ 15/15 exercises
- Create classes
- Use inheritance
- Implement polymorphism
- Master OOP concepts

### Day 4: ✅ 15/15 exercises
- Write decorators
- Use context managers
- Handle exceptions
- Work with files

### Day 5: ✅ 15/15 exercises
- Implement design patterns
- Understand SOLID principles
- Write maintainable code
- Apply patterns to problems

### Day 6: ✅ 30/30 exercises
- Implement sorting algorithms
- Solve DSA problems
- Use two pointers
- Apply dynamic programming

### Day 7: ✅ 5/5 projects
- Build real applications
- Integrate concepts
- Create portfolio pieces
- Deploy projects

---

## 💡 Tips for Success

1. **Code Every Day** - Consistency is key
2. **Type, Don't Copy** - Build muscle memory
3. **Understand, Don't Memorize** - Learn concepts
4. **Debug Actively** - Use print(), debugger
5. **Read Error Messages** - They tell you what's wrong
6. **Google is Your Friend** - Search for solutions
7. **Ask Questions** - Use Stack Overflow
8. **Build Projects** - Apply what you learn

---

## 🏆 Completion Criteria

### Beginner Level (Day 1-2)
- ✅ Understand Python syntax
- ✅ Use data structures
- ✅ Write functions
- ✅ Handle basic I/O

### Intermediate Level (Day 3-4)
- ✅ Master OOP
- ✅ Use advanced features
- ✅ Handle exceptions
- ✅ Work with files

### Advanced Level (Day 5-6)
- ✅ Implement patterns
- ✅ Solve algorithms
- ✅ Optimize code
- ✅ Write clean code

### Expert Level (Day 7)
- ✅ Build real projects
- ✅ Integrate libraries
- ✅ Deploy applications
- ✅ Portfolio ready

---

## 📈 Progress Tracking

```bash
# Check progress
python3 -m pytest day1-basics/tests/ -v --tb=no
python3 -m pytest day2-data-structures/tests/ -v --tb=no
python3 -m pytest day3-oop/tests/ -v --tb=no
python3 -m pytest day4-advanced/tests/ -v --tb=no
python3 -m pytest day5-design-patterns/tests/ -v --tb=no
python3 -m pytest day6-algorithms/tests/ -v --tb=no

# Run all tests
python3 -m pytest --tb=no -q
```

---

## 🎓 After Completion

You'll be ready for:
- ✅ Python developer roles
- ✅ Backend development
- ✅ Data analysis
- ✅ Automation scripting
- ✅ Web development
- ✅ Technical interviews

---

## 🚀 Get Started Now!

```bash
cd day1-basics
cat README.md
python3 -m pytest tests/ -v
vim src/basics.py
```

**Let's master Python in 7 days!** 🐍💪
