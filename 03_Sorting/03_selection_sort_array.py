

#  SELECTION SORT 


'''

selection  sort are also comparison based sortin algorithm that :
repeatadly select the smallest number 
and swap the starting indexx


they are devide into :

left --> sorted part 
right --> unsorted part 


'''


def selection_sort(arr):
    if not arr:
        return []
    
    n = len(arr)

    for i in range(n):
        min_idx = i
        for j in range(i+1 , n):
            if arr[j] < arr[min_idx] :
                min_idx = j
        arr[i] , arr[min_idx] = arr[min_idx] , arr[i]



arr = [23,12,14,13,56,52,62,13]

selection_sort(arr)
print(arr)