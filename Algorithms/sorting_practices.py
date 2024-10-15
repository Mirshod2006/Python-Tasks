def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def insertion_sort(arr):
    # print(*arr)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j] :
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
        # print(*arr)
    # print('\n')
    return arr
def selection_sort(arr):
    for i in range(len(arr)):
        min_ind = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_ind]:
                min_ind = j
        arr[min_ind],arr[i] = arr[i],arr[min_ind]
    return arr
array = [5,4,3,7,2,10,1]
print(selection_sort(array))  # Output: [1, 2, 3, 4, 5, 7, 10]