# LINEARITHMIC TIME COMPLEXITY – O(n log n)
# Appears mainly in Divide and Conquer algorithms
# Merge Sort, Heap Sort, Quick Sort


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]

    return result   


# Example
arr = [5, 2, 9, 1, 5, 6]
sorted_arr = merge_sort(arr)
print(sorted_arr)
