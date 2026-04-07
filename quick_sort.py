"""
Quick Sort

- sorts an array from the lowest value to the highest value
- how it works:
    - choose the first value as the pivot
    - create two new arrays:
        - values smaller than the pivot
        - values greater than or equal to the pivot
    - quick sort both arrays recursively
    - combine: sorted smaller + pivot + sorted greater
- tradeoffs:
    - very easy to read and teach
    - not in-place (creates many temporary arrays)
    - usually uses more memory than in-place quick sort
    - can be slower on large inputs because of extra allocations
- Big-O:
    - worst case: O(n²)
    - average case: O(n log n)
    - best case: O(n log n)
"""


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]

    smaller = []
    greater = []

    for x in arr[1:]:
        if x < pivot:
            smaller.append(x)
        else:
            greater.append(x)

    return quick_sort(smaller) + [pivot] + quick_sort(greater)

numbers = [5, 9, 7, 3, 10, 8, 1, 6, 4, 2]

print(quick_sort(numbers))
