"""Day 2: Data Structures Tests"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../src'))
from data_structures import *

def test_list_slice():
    assert list_slice([1,2,3,4,5], 1, 3) == [2,3]

def test_list_reverse():
    lst = [1,2,3]
    list_reverse(lst)
    assert lst == [3,2,1]

def test_list_rotate():
    assert list_rotate([1,2,3,4,5], 2) == [4,5,1,2,3]

def test_list_chunk():
    assert list_chunk([1,2,3,4,5], 2) == [[1,2], [3,4], [5]]

def test_list_zip_with():
    assert list_zip_with([1,2,3], [4,5,6], lambda x,y: x+y) == [5,7,9]

def test_dict_merge():
    assert dict_merge({"a":1}, {"b":2}) == {"a":1, "b":2}

def test_dict_invert():
    assert dict_invert({"a":1, "b":2}) == {1:"a", 2:"b"}

def test_dict_filter():
    assert dict_filter({"a":1, "b":2, "c":3}, lambda k,v: v > 1) == {"b":2, "c":3}

def test_dict_group_by():
    result = dict_group_by([1,2,3,4,5], lambda x: x % 2)
    assert result[0] == [2,4] and result[1] == [1,3,5]

def test_dict_frequency():
    assert dict_frequency([1,2,2,3,3,3]) == {1:1, 2:2, 3:3}

def test_set_union():
    assert set_union({1,2}, {2,3}) == {1,2,3}

def test_set_intersection():
    assert set_intersection({1,2,3}, {2,3,4}) == {2,3}

def test_set_difference():
    assert set_difference({1,2,3}, {2,3,4}) == {1}

def test_set_symmetric_difference():
    assert set_symmetric_difference({1,2,3}, {2,3,4}) == {1,4}

def test_is_subset():
    assert is_subset({1,2}, {1,2,3}) == True

def test_squares_comprehension():
    assert squares_comprehension(5) == [0,1,4,9,16,25]

def test_even_squares():
    assert even_squares(5) == [0,4,16]

def test_dict_comprehension():
    assert dict_comprehension(['a','b'], [1,2]) == {'a':1, 'b':2}

def test_nested_comprehension():
    assert nested_comprehension([[1,2],[3,4]]) == [1,2,3,4]

def test_conditional_comprehension():
    assert conditional_comprehension([1,5,3,8,2], 4) == [0,5,0,8,0]
