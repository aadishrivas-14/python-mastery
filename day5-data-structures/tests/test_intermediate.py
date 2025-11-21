"""Tests for Intermediate Data Structures"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../src'))

from intermediate.bst import BST
from intermediate.avl_tree import AVLTree
from intermediate.red_black_tree import RedBlackTree
from intermediate.min_heap import MinHeap
from intermediate.max_heap import MaxHeap
from intermediate.trie import Trie
from intermediate.union_find import UnionFind
from intermediate.segment_tree import SegmentTree

# BST Tests
def test_bst_insert():
    bst = BST()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    assert len(bst) == 3

def test_bst_search():
    bst = BST()
    bst.insert(5)
    bst.insert(3)
    assert bst.search(3) == True
    assert bst.search(10) == False

def test_bst_delete():
    bst = BST()
    bst.insert(5)
    bst.insert(3)
    bst.delete(3)
    assert bst.search(3) == False

def test_bst_inorder():
    bst = BST()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    assert bst.inorder() == [3, 5, 7]

# AVL Tree Tests
def test_avl_insert():
    avl = AVLTree()
    avl.insert(10)
    avl.insert(20)
    avl.insert(30)
    assert avl.search(20) == True

def test_avl_balance():
    avl = AVLTree()
    avl.insert(1)
    avl.insert(2)
    avl.insert(3)
    # Should auto-balance
    assert avl.search(2) == True

# Red-Black Tree Tests
def test_rb_tree_insert():
    rb = RedBlackTree()
    rb.insert(10)
    rb.insert(20)
    rb.insert(30)
    assert rb.search(20) == True

# Min Heap Tests
def test_min_heap_insert():
    heap = MinHeap()
    heap.insert(5)
    heap.insert(3)
    heap.insert(7)
    assert len(heap) == 3

def test_min_heap_extract():
    heap = MinHeap()
    heap.insert(5)
    heap.insert(3)
    heap.insert(7)
    assert heap.extract_min() == 3

def test_min_heap_peek():
    heap = MinHeap()
    heap.insert(5)
    heap.insert(3)
    assert heap.peek() == 3

# Max Heap Tests
def test_max_heap_insert():
    heap = MaxHeap()
    heap.insert(5)
    heap.insert(3)
    heap.insert(7)
    assert len(heap) == 3

def test_max_heap_extract():
    heap = MaxHeap()
    heap.insert(5)
    heap.insert(3)
    heap.insert(7)
    assert heap.extract_max() == 7

# Trie Tests
def test_trie_insert():
    trie = Trie()
    trie.insert("hello")
    trie.insert("world")
    assert trie.search("hello") == True

def test_trie_search():
    trie = Trie()
    trie.insert("hello")
    assert trie.search("hello") == True
    assert trie.search("hell") == False

def test_trie_starts_with():
    trie = Trie()
    trie.insert("hello")
    assert trie.starts_with("hel") == True
    assert trie.starts_with("wor") == False

def test_trie_delete():
    trie = Trie()
    trie.insert("hello")
    trie.delete("hello")
    assert trie.search("hello") == False

# Union-Find Tests
def test_union_find_union():
    uf = UnionFind(5)
    uf.union(0, 1)
    uf.union(1, 2)
    assert uf.connected(0, 2) == True

def test_union_find_find():
    uf = UnionFind(5)
    uf.union(0, 1)
    assert uf.find(0) == uf.find(1)

def test_union_find_components():
    uf = UnionFind(5)
    uf.union(0, 1)
    uf.union(2, 3)
    assert uf.count_components() == 3

# Segment Tree Tests
def test_segment_tree_query():
    arr = [1, 3, 5, 7, 9, 11]
    st = SegmentTree(arr)
    assert st.query(1, 3) == 15  # 3+5+7

def test_segment_tree_update():
    arr = [1, 3, 5, 7, 9, 11]
    st = SegmentTree(arr)
    st.update(1, 10)
    assert st.query(1, 3) == 22  # 10+5+7
