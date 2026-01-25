

# BUBBLE SORT 

'''
bubble sort is the simple comparison base sorting algorithm that :
--> adjecent element compare 
--> swap if they are wrong positonn
--> largest element bubble-up at end of the each pass

'''



def bubble_sort_bruitforce(arr):
    if not arr:
        return None
    
    n = len(arr)


    for i in range(n):
        for j in range(0 , n-i-1):
            if (arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1] , arr[j]


arr = [23,34,2,3,42,43,23,44,52]
bubble_sort_bruitforce(arr)
print(arr)
