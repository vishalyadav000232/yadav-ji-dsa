
from array import *

# Problem : Two Sum Array 

# 


#  Time-Complexity = O(n^2)


def two_sum_bruitforce(arr  , target):
    if not arr : 
        return -1
    
    for i in range(0 , len(arr)):
        for j in range (i+1 , len(arr)):
            if arr[i] + arr[j] == target:
                return [i , j]
    return -1

arr = array("i" , [73 ,3039 , 40, 50 ,63290 ])
target  = 90 # at idx 3
print(two_sum_bruitforce(arr, target))


#  


def two_sum_better(arr , target):
    

    if not arr :
        return -1
    
    temp = [(arr[i] , i) for i in range (len(arr))]
    temp.sort()

    left , right = 0 , len(arr)-1

    while left < right:
        s = temp[left][0] + temp[right][0]

        if s == target:
            return [temp[left][1] , temp[right][1]]
        elif s < target:
            left += 1
        else:
            right -= 1
        
    return -1


arr = array("i" , [73 ,3039 , 40, 50 ,630 ])
target  = 680 # at idx 3
print(two_sum_better(arr, target))




def two_sum_optimal(arr , target ):
    if not arr: 
        return -1
    
    seen = {}

    for i in range(len(arr)):
        needed = target - arr[i]

        if needed in seen:
            return [seen[needed], i]
        seen[arr[i]] = i
  

arr = array("i" , [73 ,3039 , 40, 50 ,630 ])
target  = 680 # at idx 3
print(two_sum_optimal(arr, target))
