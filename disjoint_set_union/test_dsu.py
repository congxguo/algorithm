import pytest
from dsu import dsu

def test_initial_parents():
    ds = dsu(5)
    assert ds.parent == [0, 1, 2, 3, 4]
    assert ds.rank == [0, 0, 0, 0, 0]

def test_find_singleton():
    ds = dsu(3)
    assert ds.find(0) == 0
    assert ds.find(1) == 1
    assert ds.find(2) == 2


def test_union_basic():
    ds = dsu(3)
    ds.union(0, 1)
    assert ds.find(0) == ds.find(1)
    assert ds.find(0) != ds.find(2)

def test_union_chain():
    ds = dsu(4)
    ds.union(0, 1)
    ds.union(1, 2)
    assert ds.find(0) == ds.find(2)
    assert ds.find(1) == ds.find(2)

def test_union_by_rank():
    ds = dsu(3)
    ds.union(0, 1)
    # rank[0] should increase
    assert ds.rank[ds.find(0)] == 1

    ds.union(0, 2)
    # root should still be 0
    assert ds.find(2) == ds.find(0)

def test_path_compression():
    ds = dsu(5)
    ds.union(0, 1)
    ds.union(1, 2)
    ds.union(2, 3)

    # Before compression: parent chain may be long
    root_before = ds.find(3)

    # After compression: all should point directly to root
    assert ds.parent[3] == root_before
    assert ds.parent[2] == root_before
    assert ds.parent[1] == root_before

def test_redundant_union():
    ds = dsu(3)
    ds.union(0, 1)
    root_before = ds.find(0)
    ds.union(0, 1)  # should not break anything
    assert ds.find(0) == root_before
    assert ds.find(1) == root_before