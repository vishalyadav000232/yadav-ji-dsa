













def mearg_sort(arr):

    if not arr:
        return []
    
    mid = len(arr) // 2

    left = arr[:mid]
    right = arr[mid :]

    return mearg(left , right)

def mearg(left , right):
    pass
