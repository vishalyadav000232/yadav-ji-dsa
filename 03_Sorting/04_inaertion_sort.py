



'''
Insertion sort : - insertion sort work on the sort playing card i your hand 


take one element 
place it right place in sorted part 
grow the sprted portion step by step 


Time complexity - O(n^2)

'''


def insertion_sort(arr):

    if not arr:
        return []
    
    n = len(arr)

    for i in range(1 , n):
        key = arr[i]
        j = i-1

        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j +1 ] = key

arr = [ 1 , 5,3,2]
insertion_sort(arr)

print(arr)