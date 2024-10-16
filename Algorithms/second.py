def partition(arr,left,right):
    i = left
    j = right -1
    pivot = arr[right]
    while i<j:
        while arr[i] < pivot and i < right:
            i += 1
        while j > left and arr[j] > pivot:
            j -= 1
        if i<j:
            arr[i], arr[j] = arr[j], arr[i]
    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]
    return i

def quick_sort(arr, left, right):
    if left < right:
        pivot = partition(arr, left, right)
        quick_sort(arr,left,pivot-1)
        quick_sort(arr,pivot+1, right)

arr = [33,22,88,66,55,99,11,44,77]
quick_sort(arr,0,len(arr)-1)
print(*arr)

