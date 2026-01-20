from array import *
import sys
# from numpy import *


arr = [10, 20, 30, "hello"]

for i in range(len(arr)):
    print(f"Index {i}, Value {arr[i]}, Address {id(arr[i])}")


# Pythom doe't store the element in purely contiguouse in memory like c++
#  But conceptually indexing logic are similer to .


arr = array('l', [1, 2, 3, 4, 5, 6, 7])
for i in range(0, len(arr)):
    print(arr[i], end=",")
    print(f"Index {i}, Value {arr[i]}, Address {id(arr[i])}")


copy_array = array(arr.typecode, ((x*2 for x in arr)))
for i in range(0, len(copy_array)):
    print(copy_array[i], end=",")

deleted_element = copy_array.pop(3)
print(f"deleted element : {deleted_element}")
for i in range(0, len(copy_array)):
    print(copy_array[i], end=",")

print("\n")


# new array by using the old array

new_array = arr[2:]
for i in range(0, len(new_array)):
    print(new_array[i], end=" ")

print('\n')

reverseds = arr[::-1]
for i in range(0, len(reverseds)):
    print(reverseds[i], end=" ")


# Taking input from the user and create arrary


user_array = array("i", [])

size_of_array = int(input("Enter the size of the array : "))


for i in range(0, size_of_array):
    user_array.append(int(input("Emter the element of the arrary : ")))

for val in user_array:
    print(val, end=" ")




# Create array
arr1 = [10, 20, 30, 40]

# Access
print(arr1[2])  # O(1)

# Insert at end
arr1.append(50)  # O(1)

# Insert at index
arr1.insert(1, 15)  # O(n)

# Delete
arr1.pop(2)  # O(n)

# Traverse
for x in arr1:
    print(x)



num_arr = array([2,3,5,6,"hf"])
for val in num_arr:
    print(val , end=' ')