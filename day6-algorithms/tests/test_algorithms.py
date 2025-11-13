import sys
sys.path.insert(0, '../src')
from algorithms import *

# SORTING TESTS
def test_bubble_sort():
    assert bubble_sort([64, 34, 25, 12, 22, 11, 90]) == [11, 12, 22, 25, 34, 64, 90]

def test_selection_sort():
    assert selection_sort([64, 25, 12, 22, 11]) == [11, 12, 22, 25, 64]

def test_insertion_sort():
    assert insertion_sort([12, 11, 13, 5, 6]) == [5, 6, 11, 12, 13]

def test_merge_sort():
    assert merge_sort([38, 27, 43, 3, 9, 82, 10]) == [3, 9, 10, 27, 38, 43, 82]

def test_quick_sort():
    assert quick_sort([10, 7, 8, 9, 1, 5]) == [1, 5, 7, 8, 9, 10]

# SEARCHING TESTS
def test_linear_search():
    assert linear_search([2, 3, 4, 10, 40], 10) == 3
    assert linear_search([2, 3, 4, 10, 40], 50) == -1

def test_binary_search():
    assert binary_search([2, 3, 4, 10, 40], 10) == 3
    assert binary_search([2, 3, 4, 10, 40], 50) == -1

def test_jump_search():
    assert jump_search([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 6) == 6

def test_interpolation_search():
    assert interpolation_search([10, 20, 30, 40, 50], 30) == 2

def test_exponential_search():
    assert exponential_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 7) == 6

# GRAPH TESTS
def test_bfs():
    graph = {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}
    assert bfs(graph, 2) == [2, 0, 3, 1]

def test_dfs():
    graph = {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}
    result = dfs(graph, 2)
    assert 2 in result and len(result) == 4

def test_dijkstra():
    graph = {
        0: [(1, 4), (2, 1)],
        1: [(3, 1)],
        2: [(1, 2), (3, 5)],
        3: []
    }
    distances = dijkstra(graph, 0)
    assert distances[3] == 4

def test_bellman_ford():
    graph = {
        0: [(1, -1), (2, 4)],
        1: [(2, 3), (3, 2)],
        2: [],
        3: [(1, 1)]
    }
    distances = bellman_ford(graph, 0)
    assert distances[3] == 1

def test_floyd_warshall():
    graph = [[0, 5, float('inf'), 10],
             [float('inf'), 0, 3, float('inf')],
             [float('inf'), float('inf'), 0, 1],
             [float('inf'), float('inf'), float('inf'), 0]]
    result = floyd_warshall(graph)
    assert result[0][3] == 9

# DP TESTS
def test_fibonacci_dp():
    assert fibonacci_dp(10) == 55
    assert fibonacci_dp(0) == 0

def test_knapsack():
    weights = [1, 3, 4, 5]
    values = [1, 4, 5, 7]
    assert knapsack(weights, values, 7) == 9

def test_lcs():
    assert lcs("AGGTAB", "GXTXAYB") == 4
    assert lcs("ABC", "AC") == 2

def test_lis():
    assert lis([10, 9, 2, 5, 3, 7, 101, 18]) == 4

def test_coin_change():
    assert coin_change([1, 2, 5], 11) == 3
    assert coin_change([2], 3) == -1

# DATA STRUCTURE TESTS
def test_trie():
    trie = Trie()
    trie.insert("hello")
    trie.insert("world")
    assert trie.search("hello") == True
    assert trie.search("hell") == False
    assert trie.starts_with("hel") == True

def test_min_heap():
    heap = MinHeap()
    heap.insert(3)
    heap.insert(1)
    heap.insert(6)
    heap.insert(5)
    heap.insert(2)
    assert heap.extract_min() == 1
    assert heap.extract_min() == 2

def test_bst():
    bst = BST()
    bst.insert(50)
    bst.insert(30)
    bst.insert(70)
    bst.insert(20)
    bst.insert(40)
    assert bst.search(30) == True
    assert bst.search(100) == False

def test_avl_tree():
    avl = AVLTree()
    avl.insert(10)
    avl.insert(20)
    avl.insert(30)
    assert avl.root.value == 20
    assert avl.root.left.value == 10
    assert avl.root.right.value == 30

def test_graph():
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    assert 1 in g.adj_list[0]
    assert 2 in g.adj_list[0]
