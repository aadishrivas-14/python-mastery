import sys
sys.path.insert(0, '../src')
from quant_dsa import *
import pytest

# ARRAY/STRING TESTS
def test_moving_average():
    assert moving_average([1, 2, 3, 4, 5], 3) == [2.0, 3.0, 4.0]

def test_max_profit_k_transactions():
    assert max_profit_k_transactions([3, 2, 6, 5, 0, 3], 2) == 7

def test_longest_consecutive():
    assert longest_consecutive_sequence([100, 4, 200, 1, 3, 2]) == 4

def test_merge_intervals():
    assert merge_intervals([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]

def test_rain_water():
    assert trapping_rain_water([0,1,0,2,1,0,1,3,2,1,2,1]) == 6

# MATH & PROBABILITY TESTS
def test_random_sampling():
    result = random_sampling([1,2,3,4,5], 3)
    assert len(result) == 3
    assert len(set(result)) == 3

def test_reservoir_sampling():
    stream = iter([1,2,3,4,5,6,7,8,9,10])
    result = reservoir_sampling(stream, 5)
    assert len(result) == 5

def test_shuffle():
    arr = [1,2,3,4,5]
    shuffled = shuffle_array(arr.copy())
    assert sorted(shuffled) == arr

def test_expected_value():
    outcomes = [(10, 0.5), (20, 0.3), (30, 0.2)]
    assert abs(expected_value_game(outcomes) - 17.0) < 0.01

def test_monte_carlo_pi():
    pi_estimate = monte_carlo_pi(100000)
    assert abs(pi_estimate - 3.14159) < 0.1

# DP TESTS
def test_optimal_trading():
    assert optimal_trading_strategy([1,3,2,8,4,9], 2) == 8

def test_cooldown():
    assert max_profit_with_cooldown([1,2,3,0,2]) == 3

def test_with_fee():
    assert best_time_with_fee([1,3,2,8,4,9], 2) == 8

def test_transaction_limit():
    assert stock_with_transaction_limit([3,2,6,5,0,3], 2) == 7

def test_arbitrage():
    rates = [[1, 0.5, 2], [2, 1, 4], [0.5, 0.25, 1]]
    assert arbitrage_detection(rates) == False

# GRAPH & TREE TESTS
def test_shortest_path_dag():
    graph = {0: [(1,5), (2,3)], 1: [(3,6)], 2: [(3,7)], 3: []}
    path = shortest_path_dag(graph, 0, 3)
    assert path == [0, 2, 3]

def test_topological_sort():
    result = topological_sort_tasks(4, [[1,0], [2,0], [3,1], [3,2]])
    assert result.index(0) < result.index(1)
    assert result.index(0) < result.index(2)

def test_cycle_detection():
    graph = {0: [1], 1: [2], 2: [0]}
    assert detect_cycle_directed(graph) == True

def test_mst():
    edges = [(0,1,10), (0,2,6), (0,3,5), (1,3,15), (2,3,4)]
    mst = minimum_spanning_tree(edges, 4)
    total_weight = sum(e[2] for e in mst)
    assert total_weight == 19

def test_lca():
    class TreeNode:
        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None
    
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    
    lca = lca_binary_tree(root, root.left, root.left.right)
    assert lca.val == 5

# SYSTEM DESIGN TESTS
def test_lru_cache():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    cache.put(3, 3)
    assert cache.get(2) == -1

def test_time_series_db():
    db = TimeSeriesDB()
    db.insert(1, 10.0)
    db.insert(2, 20.0)
    db.insert(3, 30.0)
    assert db.query(1, 2) == [10.0, 20.0]
    assert db.aggregate(1, 3, 'mean') == 20.0

def test_order_book_snapshot():
    ob = OrderBookSnapshot()
    ob.add_snapshot(1, {100: 10, 99: 20}, {101: 15, 102: 25})
    snapshot = ob.get_snapshot(1)
    assert snapshot is not None

def test_rate_limiter():
    limiter = RateLimiter(3, 10)
    assert limiter.allow_request(1) == True
    assert limiter.allow_request(2) == True
    assert limiter.allow_request(3) == True
    assert limiter.allow_request(4) == False

def test_circular_buffer():
    buf = CircularBuffer(3)
    buf.write(1)
    buf.write(2)
    buf.write(3)
    assert buf.is_full() == True
    assert buf.read() == 1
    assert buf.is_full() == False
