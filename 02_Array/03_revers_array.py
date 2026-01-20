

'''
Problem: Reverse an Array

Socho ek line me 5 log [a, b, c, d, e] khade hain.
Task ye hai ki unhe reverse karna hai:
[e, d, c, b, a]

Approach:
- First insaan ko last insaan ke saath swap karo
- Second insaan ko second-last ke saath swap karo
- Ye process middle tak repeat karo

Methods:
1. Two Pointer Technique (Best)
2. Using Extra Array
3. Python Built-in Methods
   - arr.reverse()
   - arr[::-1]

   arr[ :: -1]


Time Complexity ⏰  → O(n)
Space Complexity → O(1)

'''


def revers_array(arr):
    if not arr:
        return arr
    left = 0 
    right = len(arr)-1

    while left < right:
        arr[left] , arr[right] = arr[right] , arr[left]
        left +=1
        right -=1
    
    return arr



arr = [2,3,5,78,90]
reversed_arr = revers_array(arr)
print(reversed_arr)