# Day 5: Quick Start Guide

## Run Tests

```bash
cd day5-data-structures

# All tests
python3 -m pytest tests/ -v

# By category
python3 -m pytest tests/test_basic.py -v
python3 -m pytest tests/test_intermediate.py -v
python3 -m pytest tests/test_advanced.py -v
python3 -m pytest tests/test_industry.py -v

# Specific structure
python3 -m pytest tests/test_basic.py::test_stack_push -v
python3 -m pytest tests/test_basic.py -k stack -v
```

## Implementation Checklist

### Basic (8 structures)
- [ ] Stack
- [ ] Queue
- [ ] Dynamic Array
- [ ] Linked List
- [ ] Doubly Linked List
- [ ] Deque
- [ ] Circular Queue
- [ ] Hash Table

### Intermediate (8 structures)
- [ ] Min Heap
- [ ] Max Heap
- [ ] BST
- [ ] Trie
- [ ] Union-Find
- [ ] AVL Tree
- [ ] Red-Black Tree
- [ ] Segment Tree

### Advanced (9 structures)
- [ ] LRU Cache
- [ ] LFU Cache
- [ ] Bloom Filter
- [ ] Skip List
- [ ] Fenwick Tree
- [ ] B-Tree
- [ ] B+ Tree
- [ ] Suffix Array
- [ ] Rope

### Industry (5 applications)
- [ ] CDN Cache
- [ ] Call Router
- [ ] Time Series DB
- [ ] Patient DB
- [ ] Order Book

## File Locations

```
src/basic/stack.py          → tests/test_basic.py
src/intermediate/bst.py     → tests/test_intermediate.py
src/advanced/lru_cache.py   → tests/test_advanced.py
src/industry/order_book.py  → tests/test_industry.py
```

## Example Workflow

```bash
# 1. Edit file
vim src/basic/stack.py

# 2. Run tests
python3 -m pytest tests/test_basic.py -k stack -v

# 3. Fix errors, repeat

# 4. Move to next structure
```

## Progress Tracking

```bash
# Count passing tests
python3 -m pytest tests/ -v --tb=no | grep PASSED | wc -l

# See summary
python3 -m pytest tests/ -v --tb=no | tail -1
```

**Start with Stack - it's the easiest!** 🚀
