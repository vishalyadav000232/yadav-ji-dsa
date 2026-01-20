




def sum_of_all_elements(arr):
    if not arr:
        return 0
    
    sum = 0

    for val in arr:
        sum = sum + val
    return sum

arr = [1, 2, 3, 4, 5]
print(sum_of_all_elements(arr))  # Output: 15

arr = []
print(sum_of_all_elements(arr))  # Output: 0