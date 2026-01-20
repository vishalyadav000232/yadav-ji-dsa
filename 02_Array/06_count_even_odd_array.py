'''
Problem : Count even and odd numbers in an array

2️⃣ Core Concept: 

-- Traverse the array
-- Use modulo operator %
-- num % 2 == 0 → even
-- else → odd


'''

def count_even_odd(arr):
    even = 0
    odd = 0

    for val in arr:
        if val % 2 == 0:
            even +=1
        else:
            odd += 1
    return f"odd : {odd} , even : {even}"


arr = [12,34,24,23,5,3,453,2 ,1]
result = count_even_odd(arr)
print(result)