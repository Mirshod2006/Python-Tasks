def linear_search(arr,n,x):
    for i in range(n):
        if arr[i] == x:
            return i
    return -1
# Test array
arr = [3, 7, 2, 10, 5, 1,
       9, 6, 8, 4]
# Test value
x = 10
if(linear_search(arr,len(arr),x)):
    print("Element is present at index", linear_search(arr,len(arr),x)+1)
else:
    print("Element is not present in array")

def binary_search(arr,n,x):
    l = 0
    r = n-1       
    while( l <= r ):
        m = ( l+r )//2
        if( arr[m] == x):
            return m
        elif arr[m] < x:
            l = m + 1
        else:
            r = m - 1
    return -1

if(binary_search(arr,len(arr),x)):
    print("Element is present at index", binary_search(arr,len(arr),x)+1)
else:
    print("Element is not present in array")

def binarySearch(arr,low,high,x):
    mid = 0
    if high >= low:
        mid =low + (high - low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr, low, mid - 1, x)
        else:
            return binarySearch(arr, mid+1, high, x)
    else:
        return -1
    
if(binarySearch(arr,0,len(arr)-1,x)):
    print("Element is present at index", binarySearch(arr,0,len(arr)-1,x)+1)
else:
    print("Element is not present in array")