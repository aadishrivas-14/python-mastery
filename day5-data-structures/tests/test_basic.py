"""Tests for Basic Data Structures"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../src'))

from basic.dynamic_array import DynamicArray
from basic.linked_list import LinkedList
from basic.doubly_linked_list import DoublyLinkedList
from basic.stack import Stack
from basic.queue import Queue
from basic.circular_queue import CircularQueue
from basic.deque import Deque
from basic.hash_table import HashTable

# Dynamic Array Tests
def test_dynamic_array_append():
    arr = DynamicArray()
    arr.append(1)
    arr.append(2)
    assert len(arr) == 2

def test_dynamic_array_get():
    arr = DynamicArray()
    arr.append(10)
    assert arr.get(0) == 10

def test_dynamic_array_delete():
    arr = DynamicArray()
    arr.append(1)
    arr.append(2)
    arr.delete(0)
    assert len(arr) == 1

# Linked List Tests
def test_linked_list_append():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    assert len(ll) == 2

def test_linked_list_prepend():
    ll = LinkedList()
    ll.prepend(1)
    ll.prepend(2)
    assert len(ll) == 2

def test_linked_list_delete():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.delete(1)
    assert len(ll) == 1

def test_linked_list_find():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    assert ll.find(2) == True

# Doubly Linked List Tests
def test_doubly_linked_list_append():
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    assert len(dll) == 2

def test_doubly_linked_list_prepend():
    dll = DoublyLinkedList()
    dll.prepend(1)
    dll.prepend(2)
    assert len(dll) == 2

# Stack Tests
def test_stack_push():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert len(stack) == 2

def test_stack_pop():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert stack.pop() == 2

def test_stack_peek():
    stack = Stack()
    stack.push(1)
    assert stack.peek() == 1

def test_stack_is_empty():
    stack = Stack()
    assert stack.is_empty() == True

# Queue Tests
def test_queue_enqueue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    assert len(queue) == 2

def test_queue_dequeue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.dequeue() == 1

def test_queue_peek():
    queue = Queue()
    queue.enqueue(1)
    assert queue.peek() == 1

# Circular Queue Tests
def test_circular_queue_enqueue():
    cq = CircularQueue(3)
    cq.enqueue(1)
    cq.enqueue(2)
    assert len(cq) == 2

def test_circular_queue_dequeue():
    cq = CircularQueue(3)
    cq.enqueue(1)
    cq.enqueue(2)
    assert cq.dequeue() == 1

def test_circular_queue_is_full():
    cq = CircularQueue(2)
    cq.enqueue(1)
    cq.enqueue(2)
    assert cq.is_full() == True

# Deque Tests
def test_deque_add_front():
    dq = Deque()
    dq.add_front(1)
    dq.add_front(2)
    assert len(dq) == 2

def test_deque_add_rear():
    dq = Deque()
    dq.add_rear(1)
    dq.add_rear(2)
    assert len(dq) == 2

def test_deque_remove_front():
    dq = Deque()
    dq.add_front(1)
    dq.add_front(2)
    assert dq.remove_front() == 2

def test_deque_remove_rear():
    dq = Deque()
    dq.add_rear(1)
    dq.add_rear(2)
    assert dq.remove_rear() == 2

# Hash Table Tests
def test_hash_table_put():
    ht = HashTable()
    ht.put("key1", "value1")
    assert len(ht) == 1

def test_hash_table_get():
    ht = HashTable()
    ht.put("key1", "value1")
    assert ht.get("key1") == "value1"

def test_hash_table_delete():
    ht = HashTable()
    ht.put("key1", "value1")
    ht.delete("key1")
    assert len(ht) == 0

def test_hash_table_collision():
    ht = HashTable(size=1)
    ht.put("key1", "value1")
    ht.put("key2", "value2")
    assert ht.get("key1") == "value1"
    assert ht.get("key2") == "value2"
