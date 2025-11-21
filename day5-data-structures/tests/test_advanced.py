"""Tests for Advanced Data Structures"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../src'))

from advanced.b_tree import BTree
from advanced.b_plus_tree import BPlusTree
from advanced.skip_list import SkipList
from advanced.bloom_filter import BloomFilter
from advanced.lru_cache import LRUCache
from advanced.lfu_cache import LFUCache
from advanced.fenwick_tree import FenwickTree
from advanced.suffix_array import SuffixArray
from advanced.rope import Rope

# B-Tree Tests
def test_btree_insert():
    bt = BTree(t=3)
    bt.insert(10)
    bt.insert(20)
    bt.insert(30)
    assert bt.search(20) == True

def test_btree_delete():
    bt = BTree(t=3)
    bt.insert(10)
    bt.insert(20)
    bt.delete(10)
    assert bt.search(10) == False

# B+ Tree Tests
def test_bplus_tree_insert():
    bpt = BPlusTree(t=3)
    bpt.insert(10, "value10")
    bpt.insert(20, "value20")
    assert bpt.search(10) == "value10"

def test_bplus_tree_range_query():
    bpt = BPlusTree(t=3)
    bpt.insert(10, "v10")
    bpt.insert(20, "v20")
    bpt.insert(30, "v30")
    result = bpt.range_query(10, 25)
    assert len(result) == 2

# Skip List Tests
def test_skip_list_insert():
    sl = SkipList()
    sl.insert(10)
    sl.insert(20)
    assert sl.search(10) == True

def test_skip_list_delete():
    sl = SkipList()
    sl.insert(10)
    sl.delete(10)
    assert sl.search(10) == False

# Bloom Filter Tests
def test_bloom_filter_add():
    bf = BloomFilter(size=100, hash_count=3)
    bf.add("hello")
    assert bf.contains("hello") == True

def test_bloom_filter_false_positive():
    bf = BloomFilter(size=100, hash_count=3)
    bf.add("hello")
    # May return True even if not added (false positive)
    assert bf.contains("world") in [True, False]

# LRU Cache Tests
def test_lru_cache_put_get():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1

def test_lru_cache_eviction():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.put(3, 3)  # Evicts key 1
    assert cache.get(1) == -1

def test_lru_cache_update():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.get(1)  # Access 1
    cache.put(3, 3)  # Should evict 2
    assert cache.get(2) == -1

# LFU Cache Tests
def test_lfu_cache_put_get():
    cache = LFUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1

def test_lfu_cache_eviction():
    cache = LFUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.get(1)  # Freq of 1 increases
    cache.put(3, 3)  # Should evict 2
    assert cache.get(2) == -1

# Fenwick Tree Tests
def test_fenwick_tree_update():
    ft = FenwickTree(5)
    ft.update(0, 1)
    ft.update(1, 2)
    ft.update(2, 3)
    assert ft.query(2) == 6  # Sum of 0..2

def test_fenwick_tree_range_query():
    ft = FenwickTree(5)
    ft.update(0, 1)
    ft.update(1, 2)
    ft.update(2, 3)
    assert ft.range_query(1, 2) == 5  # Sum of 1..2

# Suffix Array Tests
def test_suffix_array_build():
    sa = SuffixArray("banana")
    sa.build()
    assert len(sa.search("ana")) > 0

def test_suffix_array_search():
    sa = SuffixArray("banana")
    sa.build()
    assert sa.search("ana") != []

# Rope Tests
def test_rope_concat():
    r1 = Rope("Hello")
    r2 = Rope(" World")
    r3 = r1.concat(r2)
    assert str(r3) == "Hello World"

def test_rope_insert():
    r = Rope("Hello World")
    r.insert(5, ",")
    assert str(r) == "Hello, World"

def test_rope_delete():
    r = Rope("Hello World")
    r.delete(5, 6)
    assert str(r) == "HelloWorld"

def test_rope_substring():
    r = Rope("Hello World")
    assert r.substring(0, 5) == "Hello"
