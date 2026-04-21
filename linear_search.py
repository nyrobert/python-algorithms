"""
Linear Search

- searches through an array and returns the index of the value it searches for
- Big-O:
    - worst case: O(n)
    - average case: O(n)
    - best case: O(1)
"""
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

numbers = [5, 9, 7, 3, 10, 8, 1, 6, 4, 2]

print(linear_search(numbers, 7))
print(linear_search(numbers, 11))
