"""
Selection Sort

- finds the lowest value in an array and moves it to the front of the array
- moving the next lowest values to the front, until the array is sorted
- Big-O:
    - worst case: O(n²)
    - average case: O(n²)
    - best case: O(n²)
"""
def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            # find the lowest value
            # this loop must loop through one less value each time it runs
            if arr[j] < arr[min_index]:
                min_index = j

        # move the lowest value to the front of the array
        min_value = arr.pop(min_index)
        arr.insert(i, min_value)

    return arr

numbers = [5, 9, 7, 3, 10, 8, 1, 6, 4, 2]

print(selection_sort(numbers))
