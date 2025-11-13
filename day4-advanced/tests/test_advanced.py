import sys
sys.path.insert(0, '../src')
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
