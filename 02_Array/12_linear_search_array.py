
from array import *

#  Problem : Given an array with target value  find the ind of the target value i f not present return -1 ;

#  Algorithm --> linear Search algo 


# arr --> [20 ,30 , 40, 50 ,60 ]
#  target --> 50
#  output --> 3

# Time-complexity O(n)

def linear_search(arr , target):
    if not arr :
        return -1 # epmty array 
    for i in range(0 , len(arr)):
        if arr[i] == target:
            return i
        
    return -1 # target not found !

arr = array("i" , [73 ,3039 , 40, 50 ,63290 ])
target  = 50 # at idx 3

print(linear_search(arr ,  target)) # output : 3