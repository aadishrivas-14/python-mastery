# Day 5: Custom Data Structures from Scratch

Build industry-grade data structures from the ground up. No built-in collections - pure Python implementations.

## 📚 Overview

**Total: 25 Data Structures**
- Basic: 8 structures
- Intermediate: 8 structures
- Advanced: 9 structures

---

## 🎯 Learning Objectives

- Understand how data structures work internally
- Implement core operations (insert, delete, search)
- Analyze time/space complexity
- Apply structures to real-world problems
- Optimize for industry use cases

---

## 📋 Data Structures List

### Basic Structures (8)

1. **Dynamic Array** - Auto-resizing array with amortized O(1) append
2. **Singly Linked List** - Node-based linear structure
3. **Doubly Linked List** - Bidirectional linked list
4. **Stack** - LIFO structure (array & linked list implementations)
5. **Queue** - FIFO structure (array & linked list implementations)
6. **Circular Queue** - Fixed-size ring buffer
7. **Deque** - Double-ended queue
8. **Hash Table** - Hash map with collision handling (chaining & open addressing)

### Intermediate Structures (8)

9. **Binary Search Tree (BST)** - Ordered binary tree
10. **AVL Tree** - Self-balancing BST
11. **Red-Black Tree** - Balanced BST with color properties
12. **Min Heap** - Binary heap for priority queue
13. **Max Heap** - Binary heap for maximum priority
14. **Trie (Prefix Tree)** - String search tree
15. **Disjoint Set (Union-Find)** - Connected components
16. **Segment Tree** - Range query tree

### Advanced Structures (9)

17. **B-Tree** - Multi-way search tree (database indexes)
18. **B+ Tree** - Leaf-linked B-tree (database storage)
19. **Skip List** - Probabilistic balanced structure
20. **Bloom Filter** - Probabilistic set membership
21. **LRU Cache** - Least Recently Used cache
22. **LFU Cache** - Least Frequently Used cache
23. **Fenwick Tree (BIT)** - Binary Indexed Tree for prefix sums
24. **Suffix Array** - Sorted array of suffixes
25. **Rope** - String data structure for large text editing

---

## 🏭 Industry Use Cases

### Finance (Trading Systems)
- **Order Book**: Doubly Linked List + Hash Table + Red-Black Tree
- **Price Level Management**: AVL Tree for sorted prices
- **Market Data Cache**: LRU Cache for tick data
- **Risk Aggregation**: Segment Tree for portfolio ranges
- **Trade Matching**: Priority Queue (Min/Max Heap)

### Healthcare (Medical Systems)
- **Patient Records**: B+ Tree for indexed storage
- **Appointment Scheduling**: Min Heap for priority
- **Medical History**: Rope for large text documents
- **Drug Interaction Check**: Bloom Filter for fast lookup
- **Disease Outbreak Tracking**: Disjoint Set for clusters

### Telecom (Network Systems)
- **Call Routing**: Trie for phone number prefix matching
- **Network Topology**: Graph with Union-Find
- **Packet Buffering**: Circular Queue
- **CDN Cache**: LRU/LFU Cache
- **Bandwidth Allocation**: Segment Tree for range queries

### Databases
- **Indexes**: B-Tree, B+ Tree
- **Query Cache**: LRU Cache
- **Full-Text Search**: Trie, Suffix Array
- **Transaction Log**: Circular Buffer
- **Range Queries**: Segment Tree, Fenwick Tree

### Web Services
- **Session Management**: Hash Table + LRU Cache
- **Rate Limiting**: Circular Queue + Hash Table
- **Auto-complete**: Trie
- **URL Shortener**: Hash Table + Base62 encoding
- **Load Balancing**: Consistent Hashing (Hash Ring)

---

## 📁 Structure

```
day5-data-structures/
├── src/
│   ├── basic/
│   │   ├── dynamic_array.py
│   │   ├── linked_list.py
│   │   ├── doubly_linked_list.py
│   │   ├── stack.py
│   │   ├── queue.py
│   │   ├── circular_queue.py
│   │   ├── deque.py
│   │   └── hash_table.py
│   ├── intermediate/
│   │   ├── bst.py
│   │   ├── avl_tree.py
│   │   ├── red_black_tree.py
│   │   ├── min_heap.py
│   │   ├── max_heap.py
│   │   ├── trie.py
│   │   ├── union_find.py
│   │   └── segment_tree.py
│   ├── advanced/
│   │   ├── b_tree.py
│   │   ├── b_plus_tree.py
│   │   ├── skip_list.py
│   │   ├── bloom_filter.py
│   │   ├── lru_cache.py
│   │   ├── lfu_cache.py
│   │   ├── fenwick_tree.py
│   │   ├── suffix_array.py
│   │   └── rope.py
│   └── industry/
│       ├── order_book.py          # Finance
│       ├── patient_db.py          # Healthcare
│       ├── call_router.py         # Telecom
│       ├── cdn_cache.py           # Web
│       └── time_series_db.py      # General
├── tests/
│   ├── test_basic.py
│   ├── test_intermediate.py
│   ├── test_advanced.py
│   └── test_industry.py
└── README.md
```

---

## 🚀 Quick Start

```bash
cd day5-data-structures

# Run all tests
python3 -m pytest tests/ -v

# Test specific category
python3 -m pytest tests/test_basic.py -v
python3 -m pytest tests/test_intermediate.py -v
python3 -m pytest tests/test_advanced.py -v
python3 -m pytest tests/test_industry.py -v

# Test specific structure
python3 -m pytest tests/test_basic.py::TestDynamicArray -v
```

---

## 📊 Complexity Reference

| Structure | Insert | Delete | Search | Space |
|-----------|--------|--------|--------|-------|
| Dynamic Array | O(1)* | O(n) | O(n) | O(n) |
| Linked List | O(1) | O(1) | O(n) | O(n) |
| Stack | O(1) | O(1) | O(n) | O(n) |
| Queue | O(1) | O(1) | O(n) | O(n) |
| Hash Table | O(1)* | O(1)* | O(1)* | O(n) |
| BST | O(log n)* | O(log n)* | O(log n)* | O(n) |
| AVL Tree | O(log n) | O(log n) | O(log n) | O(n) |
| Red-Black Tree | O(log n) | O(log n) | O(log n) | O(n) |
| Min/Max Heap | O(log n) | O(log n) | O(n) | O(n) |
| Trie | O(m) | O(m) | O(m) | O(n*m) |
| B-Tree | O(log n) | O(log n) | O(log n) | O(n) |
| Skip List | O(log n)* | O(log n)* | O(log n)* | O(n) |
| Bloom Filter | O(k) | N/A | O(k) | O(m) |
| LRU Cache | O(1) | O(1) | O(1) | O(n) |

*Amortized or average case

---

## 💡 Implementation Guidelines

### Each Structure Must Include:

1. **Class Definition**
   ```python
   class DataStructure:
       def __init__(self):
           # Initialize
   ```

2. **Core Operations**
   - Insert/Add
   - Delete/Remove
   - Search/Find
   - Update (if applicable)

3. **Helper Methods**
   - `__len__()` - Size
   - `__str__()` - String representation
   - `is_empty()` - Check if empty
   - `clear()` - Remove all elements

4. **Docstrings**
   - Time complexity
   - Space complexity
   - Usage examples

5. **Edge Cases**
   - Empty structure
   - Single element
   - Duplicates
   - Invalid operations

---

## 🎯 Daily Plan

### Hours 1-3: Basic Structures
- Dynamic Array, Linked Lists, Stack, Queue
- Focus on pointer manipulation
- Understand memory layout

### Hours 4-6: Intermediate Structures
- Trees (BST, AVL, Red-Black)
- Heaps, Trie
- Master recursion and balancing

### Hours 7-9: Advanced Structures
- B-Trees, Skip List, Bloom Filter
- Caches (LRU, LFU)
- Optimize for performance

### Hours 10-12: Industry Applications
- Build real-world systems
- Combine multiple structures
- Benchmark and optimize

---

## 🏆 Success Criteria

- ✅ All 25 structures implemented
- ✅ All tests passing
- ✅ Correct time/space complexity
- ✅ 5 industry use cases working
- ✅ Clean, documented code

---

## 📚 Resources

- **Visualizations**: [VisuAlgo](https://visualgo.net)
- **Practice**: [LeetCode Data Structures](https://leetcode.com/tag/data-structures/)
- **Book**: "Introduction to Algorithms" (CLRS)
- **Course**: MIT 6.006 Introduction to Algorithms

---

**Ready to build data structures from scratch? Let's go!** 🚀
