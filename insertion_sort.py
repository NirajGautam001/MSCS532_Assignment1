"""
MSCS 532 – Assignment 1
Insertion Sort in Monotonically Decreasing Order
"""

from typing import List, Sequence, TypeVar

T = TypeVar("T")

def insertion_sort_desc(arr: Sequence[T]) -> List[T]:
    """Return a new list containing *arr* sorted in strictly decreasing order."""
    a: List[T] = list(arr)          # mutable working copy
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] < key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

if __name__ == "__main__":
    sample = [23, 1, 8, 42, -5, 17]
    print("Original :", sample)
    print("Sorted ↓  :", insertion_sort_desc(sample))
