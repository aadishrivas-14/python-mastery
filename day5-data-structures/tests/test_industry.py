"""Tests for Industry Applications"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../src'))

from industry.order_book import OrderBook, Order
from industry.patient_db import PatientDB, Patient
from industry.call_router import CallRouter
from industry.cdn_cache import CDNCache
from industry.time_series_db import TimeSeriesDB

# Order Book Tests (Finance)
def test_order_book_add_order():
    ob = OrderBook()
    order = Order(1, 100.0, 10, 'BUY')
    ob.add_order(order)
    assert ob.get_best_bid() == 100.0

def test_order_book_cancel_order():
    ob = OrderBook()
    order = Order(1, 100.0, 10, 'BUY')
    ob.add_order(order)
    ob.cancel_order(1)
    assert ob.get_best_bid() is None

def test_order_book_match():
    ob = OrderBook()
    buy_order = Order(1, 100.0, 10, 'BUY')
    sell_order = Order(2, 100.0, 10, 'SELL')
    ob.add_order(buy_order)
    ob.add_order(sell_order)
    trades = ob.match_orders()
    assert len(trades) > 0

def test_order_book_spread():
    ob = OrderBook()
    ob.add_order(Order(1, 99.0, 10, 'BUY'))
    ob.add_order(Order(2, 101.0, 10, 'SELL'))
    assert ob.get_spread() == 2.0

# Patient Database Tests (Healthcare)
def test_patient_db_add():
    db = PatientDB()
    patient = Patient(1, "John Doe", 30)
    db.add_patient(patient)
    assert db.get_patient(1).name == "John Doe"

def test_patient_db_update():
    db = PatientDB()
    patient = Patient(1, "John Doe", 30)
    db.add_patient(patient)
    db.update_patient(1, age=31)
    assert db.get_patient(1).age == 31

def test_patient_db_delete():
    db = PatientDB()
    patient = Patient(1, "John Doe", 30)
    db.add_patient(patient)
    db.delete_patient(1)
    assert db.get_patient(1) is None

def test_patient_db_search_by_name():
    db = PatientDB()
    db.add_patient(Patient(1, "John Doe", 30))
    db.add_patient(Patient(2, "Jane Doe", 25))
    results = db.search_by_name("Doe")
    assert len(results) == 2

def test_patient_db_age_range():
    db = PatientDB()
    db.add_patient(Patient(1, "John", 30))
    db.add_patient(Patient(2, "Jane", 25))
    db.add_patient(Patient(3, "Bob", 40))
    results = db.get_patients_by_age_range(25, 35)
    assert len(results) == 2

# Call Router Tests (Telecom)
def test_call_router_add_route():
    router = CallRouter()
    router.add_route("1800", "toll-free")
    assert router.route_call("18001234567") == "toll-free"

def test_call_router_longest_prefix():
    router = CallRouter()
    router.add_route("1", "usa")
    router.add_route("180", "toll-free")
    router.add_route("1800", "specific-toll-free")
    assert router.route_call("18001234567") == "specific-toll-free"

def test_call_router_delete():
    router = CallRouter()
    router.add_route("1800", "toll-free")
    router.delete_route("1800")
    assert router.route_call("18001234567") is None

# CDN Cache Tests (Web)
def test_cdn_cache_put_get():
    cache = CDNCache(capacity=2)
    cache.put("/page1", "content1")
    assert cache.get("/page1") == "content1"

def test_cdn_cache_eviction():
    cache = CDNCache(capacity=2)
    cache.put("/page1", "content1")
    cache.put("/page2", "content2")
    cache.put("/page3", "content3")
    assert cache.get("/page1") is None

def test_cdn_cache_invalidate():
    cache = CDNCache(capacity=2)
    cache.put("/page1", "content1")
    cache.invalidate("/page1")
    assert cache.get("/page1") is None

def test_cdn_cache_stats():
    cache = CDNCache(capacity=2)
    cache.put("/page1", "content1")
    cache.get("/page1")
    cache.get("/page2")
    stats = cache.get_stats()
    assert stats['hits'] == 1
    assert stats['misses'] == 1

# Time Series Database Tests
def test_time_series_insert():
    db = TimeSeriesDB()
    db.insert(1000, 10.5)
    db.insert(2000, 20.5)
    result = db.query(1000, 2000)
    assert len(result) == 2

def test_time_series_query():
    db = TimeSeriesDB()
    db.insert(1000, 10.5)
    db.insert(2000, 20.5)
    db.insert(3000, 30.5)
    result = db.query(1500, 2500)
    assert len(result) == 1

def test_time_series_aggregate():
    db = TimeSeriesDB()
    db.insert(1000, 10.0)
    db.insert(2000, 20.0)
    db.insert(3000, 30.0)
    avg = db.aggregate(1000, 3000, lambda x: sum(x) / len(x))
    assert avg == 20.0

def test_time_series_delete():
    db = TimeSeriesDB()
    db.insert(1000, 10.0)
    db.insert(2000, 20.0)
    db.delete(1000, 1500)
    result = db.query(0, 3000)
    assert len(result) == 1
