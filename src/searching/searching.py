def linear_search(arr, target):
    # Your code here
    for i in arr:
        if i == target:
            return i


    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
# Binary search needs a sorted list to work
    # Your code here
    low = 0 # Gets lowest item on list
    high = len(arr) - 1 # Gets last item on list (index)

    # Continuous loop wile low is <= high
    while low <= high:
        middle = int((low + high) // 2)
        # guess = arr[middle]
        
        if arr[middle] == target:
            return middle
        elif arr[middle] > target:
            high = middle - 1 # everything from middle -1 is ignored and middle-1 becomes the new high
        elif arr[middle] < target:
            low = middle + 1

    return -1  # not found None also works

# a = [1, 2, 3, 4,5]
# print(a[len(a) -1]) # the lenght would be five, but index five is position 0 so we need to bring it to 4, give us index 4 = 5th position in a