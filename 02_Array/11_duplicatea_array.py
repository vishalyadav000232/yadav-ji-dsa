
'''
Input: A sorted array arr = [1, 1, 2, 2, 2, 3, 4, 4, 5]
Output: A new array or the same array with duplicates removed: [1, 2, 3, 4, 5]

Note: Since the array is sorted, all duplicates are consecutive. This is the key observation for an efficient solution.
'''


def remove_duplicates(arr):
    if not arr:
        return arr
    
    i = 0

    for j in range(1 , len(arr)):
        if arr[j ] != arr[i]:
            i += 1
            arr[i] = arr[j]
    return arr[:i+1]        


arr = [1, 1, 2, 2, 2, 3, 4, 4, 5]
# arr = [3, 1, 2, 3, 2, 4, 1]
result = remove_duplicates(arr)
print(result)  # Output: [1, 2, 3, 4, 5]







#  for unsorted array 



def remove_duplicates_unsorted(arr):
    if not arr:
        return []
    

    seen = set()
    result =[]
    for val in arr:
        if val not in seen:
            result.append(val)
            seen.add(val)
    return result

arr = [3, 1, 2, 3, 2, 4, 1]
print(remove_duplicates_unsorted(arr))