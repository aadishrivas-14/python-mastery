import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../src'))
from advanced import *
import asyncio
import pytest

def test_timer(capsys):
    @timer
    def slow_func():
        time.sleep(0.1)
    slow_func()
    captured = capsys.readouterr()
    assert "0.1" in captured.out or "took" in captured.out.lower()

def test_memoize():
    call_count = 0
    @memoize
    def expensive(n):
        nonlocal call_count
        call_count += 1
        return n * n
    assert expensive(5) == 25
    assert expensive(5) == 25
    assert call_count == 1

def test_retry():
    attempts = 0
    @retry(max_attempts=3)
    def flaky():
        nonlocal attempts
        attempts += 1
        if attempts < 3:
            raise ValueError("Fail")
        return "Success"
    assert flaky() == "Success"
    assert attempts == 3

def test_validate_types():
    @validate_types(x=int, y=int)
    def add(x, y):
        return x + y
    assert add(2, 3) == 5
    with pytest.raises(TypeError):
        add(2, "3")


def test_smart_file_processor_basic(tmp_path):
    """Test basic file reading"""
    f = tmp_path / "test.txt"
    f.write_text("1\n2\n3\n4\n5")

    result = list(smart_file_processor(str(f)))
    assert result == ["1", "2", "3", "4", "5"]

def test_smart_file_processor_transform(tmp_path):
    """Test with transformation function"""
    f = tmp_path / "test.txt"
    f.write_text("1\n2\n3\n4\n5")

    result = list(smart_file_processor(
        str(f),
        transform_func=lambda x: int(x) ** 2
    ))
    assert result == [1, 4, 9, 16, 25]

def test_smart_file_processor_filter(tmp_path):
    """Test with filter function"""
    f = tmp_path / "test.txt"
    f.write_text("1\n2\n3\n4\n5\n6")

    result = list(smart_file_processor(
        str(f),
        transform_func=lambda x: int(x),
        filter_func=lambda x: x % 2 == 0
    ))
    assert result == [2, 4, 6]

def test_smart_file_processor_limit(tmp_path):
    """Test with limit"""
    f = tmp_path / "test.txt"
    f.write_text("1\n2\n3\n4\n5\n6\n7\n8\n9\n10")

    result = list(smart_file_processor(
        str(f),
        transform_func=lambda x: int(x),
        limit=3
    ))
    assert result == [1, 2, 3]

def test_smart_file_processor_combined(tmp_path):
    """Test all features together"""
    f = tmp_path / "test.txt"
    f.write_text("1\n2\n3\n4\n5\n6\n7\n8\n9\n10")

    # Square numbers, keep evens, limit to 3
    result = list(smart_file_processor(
        str(f),
        transform_func=lambda x: int(x) ** 2,
        filter_func=lambda x: x % 2 == 0,
        limit=3
    ))
    assert result == [4, 16, 36]  # 2², 4², 6²

def test_smart_file_processor_empty_file(tmp_path):
    """Test with empty file"""
    f = tmp_path / "empty.txt"
    f.write_text("")

    result = list(smart_file_processor(str(f)))
    assert result == []

def test_smart_file_processor_no_matches(tmp_path):
    """Test when filter matches nothing"""
    f = tmp_path / "test.txt"
    f.write_text("1\n3\n5\n7\n9")

    result = list(smart_file_processor(
        str(f),
        transform_func=lambda x: int(x),
        filter_func=lambda x: x % 2 == 0
    ))
    assert result == []

def test_smart_file_processor_lazy_evaluation(tmp_path):
    """Test that it's truly lazy (generator)"""
    f = tmp_path / "test.txt"
    f.write_text("\n".join(str(i) for i in range(1000)))

    gen = smart_file_processor(
        str(f),
        transform_func=lambda x: int(x),
        limit=5
    )

    # Should only process 5 items, not all 1000
    result = list(gen)
    assert len(result) == 5
    assert result == [0, 1, 2, 3, 4]
def test_resource_manager_basic():
    """Test basic context manager protocol"""
    rm = ResourceManager()
    assert rm is not None

    with rm:
        pass  # Should not raise

def test_resource_manager_timing(capsys):
    """Test timing functionality"""
    with ResourceManager():
        time.sleep(0.1)

    captured = capsys.readouterr()
    assert "0.1" in captured.out or "elapsed" in captured.out.lower()

def test_resource_manager_file_operations(tmp_path):
    """Test file handling"""
    f = tmp_path / "test.txt"

    with ResourceManager(file=str(f), mode='w') as rm:
        rm.write("Hello World")

    assert f.read_text() == "Hello World"

def test_resource_manager_file_read(tmp_path):
    """Test file reading"""
    f = tmp_path / "test.txt"
    f.write_text("Test Content")

    with ResourceManager(file=str(f), mode='r') as rm:
        content = rm.read()

    assert content == "Test Content"

def test_resource_manager_transaction_commit():
    """Test transaction commit"""
    class MockDB:
        def __init__(self):
            self.committed = False
            self.rolled_back = False

        def commit(self):
            self.committed = True

        def rollback(self):
            self.rolled_back = True

    db = MockDB()

    with ResourceManager(db=db):
        pass

    assert db.committed == True
    assert db.rolled_back == False

def test_resource_manager_transaction_rollback():
    """Test transaction rollback on exception"""
    class MockDB:
        def __init__(self):
            self.committed = False
            self.rolled_back = False

        def commit(self):
            self.committed = True

        def rollback(self):
            self.rolled_back = True

    db = MockDB()

    try:
        with ResourceManager(db=db):
            raise ValueError("Test error")
    except ValueError:
        pass

    assert db.committed == False
    assert db.rolled_back == True

def test_resource_manager_locking():
    """Test lock acquisition and release"""
    with ResourceManager() as rm:
        assert rm.is_locked() == True

    # After exiting, should be unlocked
    assert rm.is_locked() == False

def test_resource_manager_combined(tmp_path, capsys):
    """Test all features together"""
    class MockDB:
        def __init__(self):
            self.committed = False

        def commit(self):
            self.committed = True

        def rollback(self):
            pass

    f = tmp_path / "test.txt"
    db = MockDB()

    with ResourceManager(file=str(f), mode='w', db=db) as rm:
        time.sleep(0.1)
        rm.write("Data")
        assert rm.is_locked() == True

    # Check all features worked
    assert f.read_text() == "Data"  # File written
    assert db.committed == True      # Transaction committed

    captured = capsys.readouterr()
    assert "0.1" in captured.out     # Timing printed

def test_resource_manager_exception_handling(tmp_path):
    """Test proper cleanup on exception"""
    class MockDB:
        def __init__(self):
            self.rolled_back = False

        def commit(self):
            pass

        def rollback(self):
            self.rolled_back = True

    f = tmp_path / "test.txt"
    db = MockDB()

    try:
        with ResourceManager(file=str(f), mode='w', db=db) as rm:
            rm.write("Partial")
            raise RuntimeError("Oops!")
    except RuntimeError:
        pass

    # Should have rolled back
    assert db.rolled_back == True
    # Lock should be released
    assert rm.is_locked() == False

def test_resource_manager_timeout():
    """Test timeout functionality"""
    with pytest.raises(TimeoutError):
        with ResourceManager(timeout=0.1):
            time.sleep(0.2)

def test_resource_manager_nested():
    """Test nested context managers"""
    with ResourceManager() as rm1:
        with ResourceManager() as rm2:
            assert rm1.is_locked() == True
            assert rm2.is_locked() == True

        assert rm1.is_locked() == True
        assert rm2.is_locked() == False

    assert rm1.is_locked() == False

def test_fibonacci_gen():
    result = list(fibonacci_gen(7))
    assert result == [0, 1, 1, 2, 3, 5, 8]

def test_prime_gen():
    result = list(prime_gen(20))
    assert result == [2, 3, 5, 7, 11, 13, 17, 19]

def test_file_reader(tmp_path):
    f = tmp_path / "test.txt"
    f.write_text("line1\nline2\nline3")
    lines = list(file_reader(str(f)))
    assert lines == ["line1", "line2", "line3"]

def test_pipeline():
    add_one = lambda x: x + 1
    double = lambda x: x * 2
    pipe = pipeline(add_one, double)
    assert pipe(5) == 12

def test_timer_context(capsys):
    with Timer():
        time.sleep(0.1)
    captured = capsys.readouterr()
    assert "0.1" in captured.out or "elapsed" in captured.out.lower()

def test_file_handler(tmp_path):
    f = tmp_path / "test.txt"
    with FileHandler(str(f), 'w') as fh:
        fh.write("test")
    assert f.read_text() == "test"

def test_transaction():
    class DB:
        def __init__(self):
            self.committed = False
            self.rolled_back = False
        def commit(self):
            self.committed = True
        def rollback(self):
            self.rolled_back = True
    
    db = DB()
    with Transaction(db):
        pass
    assert db.committed == True

def test_lock():
    lock = Lock()
    assert lock.locked == False
    with lock:
        assert lock.locked == True
    assert lock.locked == False

def test_range():
    result = list(Range(5))
    assert result == [0, 1, 2, 3, 4]
    result = list(Range(2, 5))
    assert result == [2, 3, 4]

def test_cycle():
    c = Cycle([1, 2, 3])
    result = [next(c) for _ in range(7)]
    assert result == [1, 2, 3, 1, 2, 3, 1]

def test_chain():
    result = list(Chain([1, 2], [3, 4], [5]))
    assert result == [1, 2, 3, 4, 5]

def test_zip_longest():
    result = list(ZipLongest([1, 2], [3, 4, 5], fillvalue=0))
    assert result == [(1, 3), (2, 4), (0, 5)]

@pytest.mark.asyncio
async def test_fetch_data():
    result = await fetch_data("http://test.com", delay=0.01)
    assert "test.com" in result

@pytest.mark.asyncio
async def test_gather_results():
    urls = ["http://a.com", "http://b.com"]
    results = await gather_results(urls)
    assert len(results) == 2

@pytest.mark.asyncio
async def test_with_timeout():
    async def slow():
        await asyncio.sleep(1)
        return "done"
    with pytest.raises(asyncio.TimeoutError):
        await with_timeout(slow(), 0.1)

@pytest.mark.asyncio
async def test_async_queue():
    q = AsyncQueue()
    await q.put(1)
    await q.put(2)
    assert await q.get() == 1
    assert await q.get() == 2
