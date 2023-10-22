# Binary search function to find the target element in a sorted array
def binary_search(arr, start, end, target):
    # Calculate the middle index of the current subarray
    mid = (start + end) // 2
    
    # If the start index is greater than the end index, the target is not in the array
    if start > end:
        return -1
    
    # If the middle element is less than the target, search the right half of the subarray
    if arr[mid] < target:
        return binary_search(arr, mid + 1, end, target)
    
    # If the middle element is greater than the target, search the left half of the subarray
    elif arr[mid] > target:
        return binary_search(arr, start, mid - 1, target)
    
    # If the middle element is equal to the target, return the index of the target
    elif arr[mid] == target:
        return mid

# Example array
arr = [20, 30, 40, 60, 80, 90]

# Call the binary_search function to find the target (in this case, target is 20)
ans = binary_search(arr, 0, len(arr) - 1, 20)

# Check the result of the binary search
if ans == -1:
    print("Target Not Found")
else:
    print("Target found at index", ans)
