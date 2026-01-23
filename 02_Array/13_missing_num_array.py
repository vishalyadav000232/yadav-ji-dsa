


# Probelm : find the missing number in b/w 1 - n



def find_missing_num(num , arr):
    
    if not arr or num < 2:
        return None
    

    expected_sum = num * (num + 1) // 2
    actual_sum = sum(arr)
    missing_value = expected_sum - actual_sum

    return missing_value

num = 5
arr = [1, 2, 4, 5]
print(find_missing_num(num , arr))