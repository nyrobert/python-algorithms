"""
Binary Search

- searches through a sorted array and returns the index of the value it searches for
- binary search is much faster than linear search, but requires a sorted array to work
- checks the value in the center of the array
- if the target value is lower, the next value to check is in the center of the left half of the array
- this means that the search area is always half of the previous search area
- Big-O:
    - worst case: O(log n)
    - average case: O(log n)
    - best case: O(1)
"""
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        # check value in the middle of the array
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            # search in the right half
            left = mid + 1
        else:
            # search in the left half
            right = mid - 1

    return -1

numbers = [1, 2, 3, 4, 6, 7, 8, 9, 10]

print(binary_search(numbers, 7))
print(binary_search(numbers, 11))
