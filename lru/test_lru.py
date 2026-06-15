import pytest
from lru import LRU, Node


def test_init():
    lru_cache = LRU(10)
    assert lru_cache.capacity == 10
    assert lru_cache.head.prev == None
    assert lru_cache.head.next == lru_cache.tail
    assert lru_cache.tail.prev == lru_cache.head
    assert lru_cache.tail.next == None

def test_single_put():
    lru_cache = LRU(10)
    lru_cache.put('a', 1)
    assert lru_cache.get('a').v == 1

def test_multiple_put():
    lru_cache = LRU(3)
    lru_cache.put('a', 1)
    lru_cache.put('b', 2)
    lru_cache.put('c', 3)
    assert lru_cache.get('a').v == 1
    assert lru_cache.get('b').v == 2
    assert lru_cache.get('c').v == 3
    assert lru_cache.get('4') == None

def test_full_put_1():
    lru_cache = LRU(3)
    lru_cache.put('a', 1)
    lru_cache.put('b', 2)
    lru_cache.put('c', 3)
    lru_cache.put('d', 4)
    assert lru_cache.get('a') == None
    assert lru_cache.get('b').v == 2
    assert lru_cache.get('c').v == 3
    assert lru_cache.get('d').v == 4

def test_full_put_2():
    lru_cache = LRU(3)
    lru_cache.put('a', 1)
    lru_cache.put('b', 2)
    lru_cache.put('c', 3)
    lru_cache.put('d', 4)
    lru_cache.put('e', 5)
    assert lru_cache.get('a') == None
    assert lru_cache.get('b') == None
    assert lru_cache.get('c').v == 3
    assert lru_cache.get('d').v == 4
    assert lru_cache.get('e').v == 5

def test_full_put_3():
    lru_cache = LRU(3)
    lru_cache.put('a', 1)
    lru_cache.put('b', 2)
    lru_cache.put('c', 3)
    lru_cache.get('a')
    lru_cache.put('d', 4)
    assert lru_cache.get('a').v == 1
    assert lru_cache.get('b') == None
    assert lru_cache.get('c').v == 3
    assert lru_cache.get('d').v == 4

def test_remove():
    lru_cache = LRU(3)
    lru_cache.put('a', 1)
    lru_cache.put('b', 2)
    lru_cache.put('c', 3)
    
    lru_cache.remove('a')
    lru_cache.remove('c')
    
    assert lru_cache.get('a') == None
    assert lru_cache.get('c') == None
    assert lru_cache.get('b').v == 2