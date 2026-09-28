arr1 = [4,2,7,1,5,6,8,3,9]


def partition(arr,low,high):
    pivot_idx = high
    i = low - 1

    for j in range(low,high):
        if arr[j] < arr[pivot_idx]:
           i += 1
           arr[j],arr[i] = arr[i],arr[j]

    arr[pivot_idx],arr[i+1] = arr[i+1],arr[pivot_idx]

    return i+1


def quick_sort(arr1,low,high):
    if not arr1 or len(arr1) < 1:
        return []

    if len(arr1) == 1 :
        return arr1


    if low < high:

        pivot_idx = partition(arr1,low,high)

        quick_sort(arr1,low,pivot_idx-1)
        quick_sort(arr1,pivot_idx+1,high)



    return arr1

    

print(quick_sort(arr1,0,len(arr1)-1))
    

            
            
    
