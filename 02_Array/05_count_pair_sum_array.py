













def pair_sum(arr , target):
    if not arr:
        return arr
    left = 0
    right = len(arr)-1
    current_sum = 0
    count = 0

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            count += 1
            left +=1 
            right -= 1
            print(f" the value of pair ({arr[left]} , {arr[right]})")
            

        elif current_sum < target:
            left +=1
        else:
            right +=1
    return count
        

arr = [1,2,3,4,5,6,7,8,9,12]
target = 14
result = pair_sum(arr , target)
print(result)