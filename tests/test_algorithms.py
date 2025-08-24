import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.algorithms import quicksort, binary_search

def test_quicksort():
    assert quicksort([3,1,2]) == [1,2,3]

def test_binary_search_found():
    assert binary_search([1,2,3],2) == 1

def test_binary_search_notfound():
    assert binary_search([1,2,3],5) == -1
 
