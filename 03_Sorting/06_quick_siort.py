
def partion(arr , st ,end):
    if not arr:
        return []
    i = st - 1
    piv_val = arr[end] # Choose the pivot value at last element of the array


    for j in range(st , end):
        if arr[j] < piv_val:
            i +=1
            arr[i] , arr[j] = arr[j] , arr[i]
    arr[i+1] , arr[end] = arr[end] , arr[i+1]
    return i +1


def quick_sort(arr , st , end):

    if not arr:
        return []
    
    if st < end:
        piv_indx = partion(arr ,st , end)
    # left sub array 

        quick_sort(arr , st , piv_indx-1)

    # rihgt sub array 

        quick_sort(arr , piv_indx +1 , end)






arr = [23,43,23,65,75,223]
quick_sort(arr ,  0 , len(arr)-1 )
print(arr)