"""
Bubble Sort Improved

- inner loop improvement
- stop the loop when the array is already sorted
- usage: only for learning purposes!
- Big-O:
    - worst case: O(n²)
    - average case: O(n²)
    - best case: O(n)
"""
def bubble_sort_improved(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        # inner loop must loop through one less value each time it runs
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                tmp        = arr[j]
                arr[j]     = arr[j + 1]
                arr[j + 1] = tmp

                swapped = True

        # if the outer loop goes through the array without swapping any values then the array is sorted
        if not swapped:
            break

    return arr

numbers = [5, 9, 7, 3, 10, 8, 1, 6, 4, 2]

print(bubble_sort_improved(numbers))
