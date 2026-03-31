"""
Merge Sort

- divide-and-conquer algorithm that sorts an array by first breaking it down into smaller arrays
- and then building the array back together the correct way so that it is sorted
- Big-O:
    - worst case: O(n log n)
    - average case: O(n log n)
    - best case: O(n log n)
"""
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # splits it in two sub-arrays
    # calls itself with each half of that array so that the arrays are split again recursively
    # until a sub-array only consist of one value
    mid = int(len(arr) / 2)
    left = arr[:mid]
    right = arr[mid:]

    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)

    return merge(sorted_left, sorted_right)

def merge(left, right):
    result = []
    i = 0
    j = 0

    while (i < len(left) and j < len(right)):
        if (left[i] < right[j]):
            result.append(left[i])
            i = i + 1
        else:
            result.append(right[j])
            j = j + 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

numbers = [5, 9, 7, 3, 10, 8, 1, 6, 4, 2]

print(merge_sort(numbers))
