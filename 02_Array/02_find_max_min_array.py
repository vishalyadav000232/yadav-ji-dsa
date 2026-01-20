

# Problem : Find the maximum and minimum elements in an array.

'''
Approche 🗓️

1. ❌ Dont initilized the max = 0 it fails for the negative elemens 
2. travers all element and campare with the max and min 
3. ✅ chose the array fist element for min and max
4. Time Complexity ⏰ O(n) 
5. Space Complexity O(1)


'''

from array import *
def find_min_max(arr):

    # edge cases

    if not arr:
        return None
    
    max_val = arr[0]
    min_val = arr[0]

    for i in range(0 , len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
        if arr[i] < min_val:
            min_val = arr[i]
    return min_val , max_val


# execute 

arr = array("i" , [3, 5, 1, 8, 2])
min_value , max_value = find_min_max(arr)
print(f"min value : {min_value} , max value : {max_value}")