# src/algorithms.py

def quicksort(arr):
    """
    Quicksort: returns a new sorted list.

    Complexity:
        - Average time: O(n log n)
        - Worst-case time: O(n^2) (when pivot splits are very unbalanced)
        - Space: O(n) for recursion + new lists (this simple implementation is not in-place)
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


def binary_search(arr, x):
    """
    Binary search on a sorted list. Returns the index of x, or -1 if not found.

    Requirements:
        - 'arr' must be sorted in non-decreasing order.

    Complexity:
        - Time: O(log n)
        - Space: O(1)
    """
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == x:
            return mid
        if arr[mid] < x:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
