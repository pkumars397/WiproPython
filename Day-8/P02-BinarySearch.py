# Binary search is an efficient algorithm for finding the position of a target element in a sorted list.
# It works by repeatedly dividing the search range in half.
# list must be sorted for bs to work

def binary_search(arr, target): #Time complexity : O(logn),space complexity: S(1)--takes fixed space.
    """
    Perform a binary search for a target element in a sorted list.
    :param arr: Sorted list of elements to search through
    :param target: Element to find
    :return: Index of the target element, or -1 if not found
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2  # Find the middle index  . // returns quotient

        if arr[mid] == target:
            return mid  # Target found, return the index

        elif arr[mid] < target:
            left = mid+1  # Discard the left half
        else:
            right = mid-1  # Discard the right half
    return -1  # Target not found

list=[1,2,3,4,5,20]
target=20
index=binary_search(list,target)
print(index)
if index!=-1:
    print(f'{target} is found at index {index}')
else:
    print(f'{target} not found in list')