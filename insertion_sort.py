"""
Insertion Sort

- uses one part of the array (left side) to hold the sorted values
- the other part of the array (right side) to hold values that are not sorted yet
- takes one value at a time from the unsorted part of the array
- puts it into the right place in the sorted part of the array, until the array is sorted
- Big-O:
    - worst case: O(n²)
    - average case: O(n²)
    - best case: O(n)
"""
def insertion_sort(arr):
    n = len(arr)

    # outer loop: picks a value to be sorted, skips the first value
    for i in range(1, n):
        key = arr[i]
        # previous value (on the left side)
        j = i - 1

        # inner loop: runs until the previous value is bigger than the actual value
        while arr[j] > key and j >= 0:
            # move value on the left to the right
            arr[j + 1] = arr[j]
            # move the counter to the left
            j = j - 1

        # we moved all of the bigger values to the right
        # we got the right position for the actual value (j + 1)
        arr[j + 1] = key

    return arr

numbers = [5, 9, 7, 3, 10, 8, 1, 6, 4, 2]

print(insertion_sort(numbers))
