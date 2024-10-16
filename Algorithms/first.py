def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for i in range(n-1-i):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr
any_arr = [4,3,12,51,90,75,34,21,72]
print(bubble_sort(any_arr))