



def is_sorted(arr):
    if not arr or len(arr) == 1 :
        return  True #"single array  or empty array allready sorted"
    
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True


print(is_sorted([1, 2, 3, 4, 5]))   # True
print(is_sorted([1, 3, 2, 4, 5]))   # False
print(is_sorted([5]))               # True
print(is_sorted([]))                # True
print(is_sorted([-2, -1, 0, 1]))