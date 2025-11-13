"""Day 6: Algorithms & Data Structures - 25 Exercises"""

# SORTING (5)
def bubble_sort(arr):
    """TODO: Bubble sort - O(n²)
    Hint: Compare adjacent, swap if needed"""
    pass

def selection_sort(arr):
    """TODO: Selection sort - O(n²)
    Hint: Find min, swap with first unsorted"""
    pass

def insertion_sort(arr):
    """TODO: Insertion sort - O(n²)
    Hint: Insert each element into sorted portion"""
    pass

def merge_sort(arr):
    """TODO: Merge sort - O(n log n)
    Hint: Divide, sort, merge"""
    pass

def quick_sort(arr):
    """TODO: Quick sort - O(n log n) average
    Hint: Partition around pivot"""
    pass

# SEARCHING (5)
def linear_search(arr, target):
    """TODO: Linear search - O(n)
    Hint: Check each element"""
    pass

def binary_search(arr, target):
    """TODO: Binary search - O(log n)
    Hint: Divide sorted array in half"""
    pass

def jump_search(arr, target):
    """TODO: Jump search - O(√n)
    Hint: Jump by √n, then linear"""
    pass

def interpolation_search(arr, target):
    """TODO: Interpolation search - O(log log n)
    Hint: Estimate position based on value"""
    pass

def exponential_search(arr, target):
    """TODO: Exponential search - O(log n)
    Hint: Find range, then binary search"""
    pass

# GRAPHS (5)
def bfs(graph, start):
    """TODO: Breadth-first search
    Hint: Use queue, visit level by level"""
    pass

def dfs(graph, start):
    """TODO: Depth-first search
    Hint: Use stack or recursion"""
    pass

def dijkstra(graph, start):
    """TODO: Dijkstra's shortest path
    Hint: Use priority queue, track distances"""
    pass

def bellman_ford(graph, start):
    """TODO: Bellman-Ford (handles negative weights)
    Hint: Relax edges V-1 times"""
    pass

def floyd_warshall(graph):
    """TODO: All-pairs shortest paths
    Hint: DP with 3 nested loops"""
    pass

# DYNAMIC PROGRAMMING (5)
def fibonacci_dp(n):
    """TODO: Fibonacci with DP - O(n)
    Hint: Use array to store results"""
    pass

def knapsack(weights, values, capacity):
    """TODO: 0/1 Knapsack - O(nW)
    Hint: DP table[i][w]"""
    pass

def lcs(s1, s2):
    """TODO: Longest Common Subsequence
    Hint: DP table, match or skip"""
    pass

def lis(arr):
    """TODO: Longest Increasing Subsequence
    Hint: DP array, track max length"""
    pass

def coin_change(coins, amount):
    """TODO: Minimum coins for amount
    Hint: DP array, try each coin"""
    pass

# DATA STRUCTURES (5)
class Trie:
    """TODO: Trie for string storage
    Hint: Tree with character nodes"""
    pass

class MinHeap:
    """TODO: Min heap implementation
    Hint: Array-based, parent at i//2"""
    pass

class BST:
    """TODO: Binary Search Tree
    Hint: Left < root < right"""
    pass

class AVLTree:
    """TODO: Self-balancing BST
    Hint: Track height, rotate on imbalance"""
    pass

class Graph:
    """TODO: Graph with adjacency list
    Hint: Dict of node -> [neighbors]"""
    pass
