"""
Quick Sort Improved

- sorts an array from the lowest value to the highest value
- how it works:
    - choose one value as the pivot (here: last value in the section)
    - move all values lower than or equal to the pivot to the left side
    - place the pivot between left and right sides
    - repeat the same process for the left and right sides
- why this version is better for practical use:
    - in-place partitioning (very low extra memory)
    - avoids creating many temporary arrays
    - scales better for larger lists than the simpler split-list version
- Big-O:
    - worst case: O(n²)
    - average case: O(n log n)
    - best case: O(n log n)
"""


def partition(arr, low, high):
    # choose the last value as the pivot
    pivot_value = arr[high]
    # index of the smaller value
    smaller_index = low - 1

    # move values smaller than or equal to pivot to the left side
    for current_index in range(low, high):
        if arr[current_index] <= pivot_value:
            smaller_index = smaller_index + 1

            # swap the smaller value with the current value
            temp = arr[smaller_index]
            arr[smaller_index] = arr[current_index]
            arr[current_index] = temp

    # place pivot after the last smaller value
    temp = arr[smaller_index + 1]
    arr[smaller_index + 1] = arr[high]
    arr[high] = temp

    return smaller_index + 1


def quick_sort_recursive(arr, low, high):
    if low < high:
        # partition the array and get the pivot index
        pivot_index = partition(arr, low, high)

        # recursively sort the left and right sides
        quick_sort_recursive(arr, low, pivot_index - 1)
        # recursively sort the right side
        quick_sort_recursive(arr, pivot_index + 1, high)


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    quick_sort_recursive(arr, 0, len(arr) - 1)
    return arr


numbers = [5, 9, 7, 3, 10, 8, 1, 6, 4, 2]

print(quick_sort(numbers))
