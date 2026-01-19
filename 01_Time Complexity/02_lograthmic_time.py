

# Logarithmic Time Complexity - O(log n)
# Very fast search technique (Binary Search)
# Binary search works on the sorted array 

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1  

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# Example ()
binary_array_list = [3, 4, 12, 21, 23, 23, 34 ,3432]
target = 23

target_location = binary_search(binary_array_list, target)
print(target_location)


# Binary search -->


'''
n = 100 steps
linear search  - 100 steps
binary search -  100 // 2 = 50 
                 50 // 2 = 25
                 25 // 2 = 12
                 12 // 2 = 6
                 6 // 2 = 3
                 3 // 2 = 1
                 1 // 2 = 0

'''