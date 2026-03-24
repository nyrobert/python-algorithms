"""
Bubble Sort

- sorts an array from the lowest value to the highest value
- how it works:
    - go through the array, one value at a time
    - for each value, compare the value with the next value
    - if the value is higher than the next one, swap the values so that the highest value comes last
    - go through the array as many times as there are values in the array
- usage: only for learning purposes!
- Big-O:
    - worst case: O(n²)
    - average case: O(n²)
    - best case: O(n²)
"""
def bubble_sort(arr):
    n = len(arr)

    # outer loop: controls how many times the inner loop must run
    for i in range(n):
        # inner loop: goes through the array and swaps values if the first value is higher than the next value
        for j in range(n - 1):
            if arr[j] > arr[j + 1]:
                tmp        = arr[j]
                arr[j]     = arr[j + 1]
                arr[j + 1] = tmp

    return arr

numbers = [5, 3, 8, 4, 2]

print(bubble_sort(numbers))
