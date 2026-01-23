

# Problem : Move the all zero at the end 


# Bruit-force
# better
# optimized




def move_all_zero_end(arr):
    if not arr:
        return -1
    
    result = []
    count_zero = 0
    for val in arr:
        if val != 0:
            result.append(val)
        else:
            count_zero += 1
    result.extend([0] * count_zero)

    return result


arr = [1, 0, 2, 0, 0, 3, 4]
print(move_all_zero_end(arr))



def move_zeros_better(arr):
    if not arr:
        return None
    j = 0 # this is for the hold the non zero value 

    for i in range(len(arr)):
        if arr[i] != 0:
            arr[j] = arr[i]
            j += 1
        

    while j < len(arr):
            arr[j] = 0
            j +=1

    return arr


arr = [1, 0, 2, 0, 0, 3, 4]
print(move_zeros_better(arr))




def move_zeros_optimal(arr):
    if not arr:
        return None
    j = 0
    for i in range(len(arr)):
        if arr[i] != 0 :
            arr[i] = arr[j]
            arr[j] = arr[i]
            j  += 1
        
    return arr

arr = [1, 0, 2,0,30,0,0,365,32, 0, 0, 3, 4]
print(move_zeros_optimal(arr))