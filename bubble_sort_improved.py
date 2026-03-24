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
        isSwap = False

        # inner loop must loop through one less value each time it runs
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                tmp        = arr[j]
                arr[j]     = arr[j + 1]
                arr[j + 1] = tmp

                isSwap = True

        # if the outer loop goes through the array without swapping any values then the array is sorted
        if not isSwap:
            break

    return arr

numbers = [5, 3, 8, 4, 2]

print(bubble_sort_improved(numbers))
