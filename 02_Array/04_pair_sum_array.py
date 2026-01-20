'''
Problem: Pair Sum

Given a sorted array:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 12]
and a target = 17

Find a pair of elements whose sum is equal to the target.

Methods:
1. Two Pointer Approach (Optimized)
2. Nested Loop Approach (Brute Force)


'''


def pair_sum(arr , target):
    if not arr:
        return arr
    left = 0
    right = len(arr)-1
    current_sum = 0

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            return f" the value of pair ({arr[left]} , {arr[right]})"
        elif current_sum < target:
            left +=1
        else:
            right +=1
    return " No pair found"
        

arr = [1,2,3,4,5,6,7,8,9,12]
target = 149
result = pair_sum(arr , target)
print(result)



#  Time Complexity - O(n2)

def pair_sum_bruitforce(arr , target):
    if not arr:
        return arr
    
    n = len(arr)
    for  i in range (0 , n):
        for j in range( i+1 , n):
            if arr[i] + arr[j] == target:
                return (arr[i], arr[j])
            
    return "NO pair found !"


arr = [1,2,3,4,5,6,7,8,9,12]
target = 14
result = pair_sum_bruitforce(arr , target)
print(result)