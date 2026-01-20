

'''
We want to know how many times each element occurs.

Think of it like counting cards in a deck:

Go through each element and increment its count
'''
def count_frequency(arr):
    frq = {}
    for x in arr:
        if x in frq:
            frq[x] += 1
        else: 
            frq[x] = 1
    return frq

arr = [1, 2, 2, 3, 1, 2, 4]
print(count_frequency(arr))