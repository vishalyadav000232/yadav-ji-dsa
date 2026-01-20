'''
Problem : Second largest element in the array 
arr = [10, 20, 4, 45, 99]
first larg = 99 
second == 45


'''




def second_largeset_elements(arr):
    if not arr or len(arr) < 2:
        return "not enought to find"
    
    first  = float("-inf")
    second  = float("-inf")

    for val in arr:
        if val > first:
            second = first
            first = val

        elif val > second and val!=first:
            second = val
    if second == float("-inf"):
        return "all element are the same "
    return second

  

arr = [10, 76, 4, 45, 99]
result = second_largeset_elements(arr)
print(result)