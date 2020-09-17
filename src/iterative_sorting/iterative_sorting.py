# TO-DO: Complete the selection_sort() function below
# Source Ref - https://www.w3resource.com/python-exercises/python-basic-exercise-91.php
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1): # we end the array one index short, because we will call it ourselves by adding 1
        cur_index = i 
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for j in range(i+1, len(arr)):# Getting the second index after i by adding 1 to it.
            if arr[j] < arr[i]:
                smallest_index = j # smallest value of i & j is located at index j
        # TO-DO: swap
        # Your code here
        curr_lowest = arr[smallest_index]
        arr[smallest_index] = arr[i]
        arr[i] = curr_lowest
    return arr
#  0 1 2 3 4 5
#  6 4 3 1 5 7
#  4 3 1 5 6 74

#  0 1 2 3 4 5
#  3 4 
# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    swapped = True
    while swapped: # keeps iterating while a swap happened
        swapped = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1]
                swapped = True

    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
