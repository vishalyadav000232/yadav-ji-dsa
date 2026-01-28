

'''
✅ HEAP SORT 

This is the comparison based sorting algorithm :

max heap -->  root element is the largest
min heap -->  root element is the smallest

heap sort main idea : -

part-1 --> Building a max heap 

part-2 --> Root (max element) ko last element se swap karo
           Heap ka size reduce karo
           Fir heapify karo





'''


def heapify(arr , n , i):
    if not arr or n <=1:
        return -1
    
    largest = i
    left = 2*i +1 
    right = 2*i +2


    if left < n and arr[left] > arr[largest]: # agar left chils of parent node bada h to 
        largest = left

    if right < n and arr[right] > arr[largest]: # agar right child of the parent node bada h to 
        largest = right
    if largest != i: # agar largest not equal to i then swap 
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr ):
    if not arr:
        return []
    
    n = len(arr)

    # Build the max-heap 

    for i in range (n//2-1 , -1 , -1):
        heapify(arr , n , i)


    # Extract the element to sort 

    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]   # max element goes to end
        heapify(arr, i, 0)                # heapify root with reduced heap size

    return arr

arr = [4, 10, 3, 5, 1]
print(heap_sort(arr))