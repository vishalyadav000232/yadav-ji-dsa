




def three_sum(arr):
    if not arr:
        return -1
    
    result = []
    for i in range(0 , len(arr)):
        for j in range( i +1 , len(arr)):
            for k in range (j +1 , len(arr)):

                if arr[i] + arr[j] + arr[k] ==0:
                    triplet = sorted([arr[i], arr[j], arr[k]])  # sort to handle duplicates
                    if triplet not in result:
                        result.append(triplet)
                
    return result

# arr = [-1,0,1,2,-1,-4]
# print(three_sum(arr))



def three_sum_optimal(arr):

    if not arr:
        return -1
    
    arr.sort()
    n = len(arr)
    result = []

    for i in range(0 , n-2):
        
        if i > 0 and arr[i] == arr[i -1]:
            continue
        left = i +1 
        right = n -1

        while left < right:
            total = arr[i] + arr[left] + arr[right]

            if total == 0:
                result.append([arr[i] , arr[left] , arr[right]])
                left += 1
                right -= 1

                while left < right and arr[left]== arr[left-1]:
                    left +=1
                while left < right and arr[right]== arr[right+1]:
                    right -=1

            elif total < 0:
                left += 1
            else:
                right -= 1

    return result


arr = [-1,0,1,2,-1,-4]
print(three_sum_optimal(arr))