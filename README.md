# Python Mastery in 7 Days - Zero to Hero

Complete Python mastery roadmap: From absolute beginner to advanced patterns and algorithms in one week!

## 📊 Overview

- **Day 1:** Python Basics (20 exercises)
- **Day 2:** Data Structures (20 exercises)
- **Day 3:** Object-Oriented Programming (15 exercises)
- **Day 4:** Advanced Python (20 exercises)
- **Day 5:** Design Patterns (15 exercises)
- **Day 6:** Algorithms & Data Structures (25 exercises)
- **Day 7:** Quantitative Finance Projects (5 projects)
- **Day 8:** DSA for Quant Interviews (25 problems)

**Total: 115 exercises + 5 quant projects + 25 quant DSA problems**

---

## 🎯 Quick Start

```bash
# Setup virtual environment
python3 -m venv venv
source venv/bin/activate  # Linux/Mac (Windows: venv\Scripts\activate)
pip install -r requirements.txt

# Day 1 - Start here!
cd day1-basics
python3 -m pytest tests/ -v

# Implement functions in src/
vim src/basics.py

# Test specific exercise
python3 -m pytest tests/test_basics.py::test_hello_world -v
```

See [SETUP.md](SETUP.md) for detailed setup instructions.

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
- Magic methods (`__add__`, `__len__`, etc.)
- Singleton pattern

**Exercises:** Person, BankAccount, Rectangle, Student, Counter, Animal hierarchy, Vehicle system, Vector, Book, Stack, Temperature, Singleton

**Time:** 6-8 hours

---

### Day 4: Advanced Python (20 exercises)
**Topics:**
- Decorators (function, class)
- Generators and yield
- Context managers (`with` statement)
- Iterators protocol
- Async/await basics
- Exception handling
- File operations
- Regular expressions

**Exercises:** timer, memoize, retry, validate_types, fibonacci_gen, prime_gen, file_reader, pipeline, Timer, FileHandler, Transaction, Lock, Range, Cycle, Chain, ZipLongest, fetch_data, gather_results, with_timeout, AsyncQueue

**Time:** 6-8 hours

---

### Day 5: Design Patterns (15 exercises)
**Topics:**
- Creational: Singleton, Factory, Builder, Prototype
- Structural: Adapter, Decorator, Facade, Proxy
- Behavioral: Observer, Strategy, Command, State, Iterator, Template Method, Chain of Responsibility

**Exercises:** Implement 15 design patterns with real-world examples

**Time:** 6-8 hours

---

### Day 6: Algorithms & Data Structures (25 exercises)
**Topics:**
- Sorting (bubble, selection, insertion, merge, quick)
- Searching (linear, binary, jump, interpolation, exponential)
- Graphs (BFS, DFS, Dijkstra, Bellman-Ford, Floyd-Warshall)
- Dynamic Programming (fibonacci, knapsack, LCS, LIS, coin_change)
- Data Structures (Trie, MinHeap, BST, AVL, Graph)

**Exercises:** 25 algorithm implementations covering sorting, searching, graphs, DP, and advanced data structures

**Time:** 8-10 hours

---

### Day 7: Quantitative Finance Projects (5 projects)
**Projects:**
1. **Options Pricer** - Black-Scholes, Greeks, implied volatility, binomial trees
2. **Market Simulator** - Order book, matching engine, market making
3. **Risk Calculator** - VaR, CVaR, stress testing, portfolio risk
4. **Backtesting Engine** - Strategy testing, Sharpe/Sortino, equity curves
5. **Portfolio Optimizer** - Mean-variance, efficient frontier, risk parity, Black-Litterman

**Time:** 10-12 hours

---

### Day 8: DSA for Quant Interviews (25 problems)
**Topics:**
- Array/String: moving_average, max_profit_k_transactions, longest_consecutive, merge_intervals, rain_water
- Math/Probability: random_sampling, reservoir_sampling, shuffle_array, expected_value, monte_carlo_pi
- Dynamic Programming: optimal_trading, max_profit_cooldown, best_time_with_fee, stock_with_transaction_limit, arbitrage_detection
- Graph/Tree: shortest_path_dag, topological_sort, detect_cycle, mst, lca
- System Design: LRUCache, TimeSeriesDB, OrderBookSnapshot, RateLimiter, CircularBuffer

**Exercises:** 25 quant-specific DSA problems commonly asked in HFT/trading interviews

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
│   ├── task-manager/
│   │   ├── src/task_manager.py
│   │   ├── tests/
│   │   ├── requirements.txt
│   │   └── README.md
│   ├── web-scraper/
│   │   ├── src/scraper.py
│   │   ├── tests/
│   │   ├── requirements.txt
│   │   └── README.md
│   ├── rest-api/
│   │   ├── src/api.py
│   │   ├── tests/
│   │   ├── requirements.txt
│   │   └── README.md
│   ├── data-analyzer/
│   │   ├── src/analyzer.py
│   │   ├── tests/
│   │   ├── requirements.txt
│   │   └── README.md
│   └── chat-server/
│       ├── src/server.py
│       ├── src/client.py
│       ├── tests/
│       ├── requirements.txt
│       └── README.md
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
- Master magic methods

### Day 4: ✅ 20/20 exercises
- Write decorators
- Use generators
- Create context managers
- Work with async/await

### Day 5: ✅ 15/15 exercises
- Implement design patterns
- Understand SOLID principles
- Write maintainable code
- Apply patterns to problems

### Day 6: ✅ 25/25 exercises
- Implement sorting algorithms
- Master searching techniques
- Solve graph problems
- Apply dynamic programming
- Build advanced data structures

### Day 7: ✅ 5/5 projects
- Build quant finance applications
- Implement pricing models
- Calculate risk metrics
- Optimize portfolios

### Day 8: ✅ 25/25 problems
- Solve quant-specific DSA problems
- Master probability algorithms
- Implement system designs
- Optimize for HFT interviews

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

### Expert Level (Day 7-8)
- ✅ Build quant projects
- ✅ Implement pricing models
- ✅ Solve quant DSA problems
- ✅ HFT interview ready

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
