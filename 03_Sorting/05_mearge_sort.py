def divide(arr, left, right):
    if left < right:
        mid = (left + right) // 2

        divide(arr, left, mid)
        divide(arr, mid + 1, right)

        merge(arr, left, mid, right)


def merge(arr, left, mid, right):
    result = []

    i = left
    j = mid + 1

    # merge two sorted halves
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            result.append(arr[i])
            i += 1
        else:
            result.append(arr[j])
            j += 1

    # remaining elements
    while i <= mid:
        result.append(arr[i])
        i += 1

    while j <= right:
        result.append(arr[j])
        j += 1

    
    arr[left:right + 1] = result
#
                          
arr = [5, 3, 2, 8, 1]
divide(arr, 0, len(arr) - 1)
print(arr)
