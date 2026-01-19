


'''
 Exponential time complexity O(3^n)
 it create no. of the double opration on any extra input 

 n= 5   --->  32 steps
 n = 10 --->  1023 steps
 n = 20 --->  1,048,576 steps
 n = 30 ---> 1,073,741,824 steps (large operations )
'''



def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)


result = fib(5)
print(result)